"""
DIJKSTRA SARGUZASHT O'YINI
Eng qisqa yo'l topish vizualizatsiyasi - Creative versiya

Muallif: GitHub Copilot
Sana: 2025-12-14
"""

import pygame
import heapq
import math
import random
import time
from enum import Enum
from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass


# ==================== KONSTANTALAR ====================
class Colors:
    """Barcha ranglar"""
    # Asosiy
    WHITE = (255, 255, 255)
    BLACK = (30, 30, 30)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (240, 240, 240)
    DARK_GRAY = (50, 50, 50)

    # Yo'l ranglari
    ROAD_HIGHWAY = (120, 120, 120)      # Avtomobil - kulrang
    ROAD_BIKE = (46, 204, 113)          # Velosiped - yashil
    ROAD_WALK = (241, 196, 15)          # Piyoda - sariq
    ROAD_MOUNTAIN = (139, 90, 43)       # Tog' - jigarrang
    ROAD_BRIDGE = (52, 152, 219)        # Ko'prik - ko'k
    ROAD_TUNNEL = (44, 62, 80)          # Tunnel - qora

    # Joy ranglari
    LOCATION_HOME = (231, 76, 60)       # Uy - qizil
    LOCATION_SHOP = (155, 89, 182)      # Do'kon - binafsha
    LOCATION_SCHOOL = (52, 152, 219)    # Maktab - ko'k
    LOCATION_HOSPITAL = (255, 255, 255) # Kasalxona - oq
    LOCATION_PARK = (46, 204, 113)      # Park - yashil
    LOCATION_CAFE = (230, 126, 34)      # Kafe - to'q sariq

    # Holat ranglari
    NODE_START = (46, 204, 113)
    NODE_END = (231, 76, 60)
    NODE_VISITED = (155, 89, 182)
    NODE_CURRENT = (241, 196, 15)
    NODE_PATH = (241, 196, 15)
    NODE_HOVER = (174, 214, 241)

    # UI
    PANEL_BG = (44, 62, 80)
    PANEL_LIGHT = (52, 73, 94)
    BUTTON_GREEN = (39, 174, 96)
    BUTTON_RED = (192, 57, 43)
    BUTTON_BLUE = (52, 152, 219)
    BUTTON_ORANGE = (230, 126, 34)
    BUTTON_PURPLE = (155, 89, 182)
    TEXT_WHITE = (255, 255, 255)

    # Canvas
    CANVAS_BG = (236, 240, 241)
    GRID_LINE = (220, 220, 220)

    # Effektlar
    STAR_YELLOW = (255, 215, 0)
    CONFETTI = [(231, 76, 60), (46, 204, 113), (52, 152, 219),
                (241, 196, 15), (155, 89, 182), (230, 126, 34)]


# ==================== YO'L TURLARI ====================
class RoadType(Enum):
    """Yo'l turlari va ularning xususiyatlari"""
    HIGHWAY = ("Avtomobil yo'li", 1, Colors.ROAD_HIGHWAY, 8, False)
    BIKE = ("Velosiped yo'li", 2, Colors.ROAD_BIKE, 5, False)
    WALK = ("Piyoda yo'li", 3, Colors.ROAD_WALK, 4, True)  # Nuqtali
    MOUNTAIN = ("Tog' yo'li", 5, Colors.ROAD_MOUNTAIN, 6, False)
    BRIDGE = ("Ko'prik", 2, Colors.ROAD_BRIDGE, 7, False)
    TUNNEL = ("Tunnel", 4, Colors.ROAD_TUNNEL, 6, False)

    def __init__(self, display_name, weight, color, width, dashed):
        self.display_name = display_name
        self.weight = weight
        self. color = color
        self.width = width
        self.dashed = dashed


# ==================== JOY TURLARI ====================
class LocationType(Enum):
    """Joy turlari"""
    HOME = ("Uy", "🏠", Colors.LOCATION_HOME)
    SHOP = ("Do'kon", "🏪", Colors.LOCATION_SHOP)
    SCHOOL = ("Maktab", "🏫", Colors.LOCATION_SCHOOL)
    HOSPITAL = ("Kasalxona", "🏥", Colors.LOCATION_HOSPITAL)
    PARK = ("Park", "🌳", Colors.LOCATION_PARK)
    CAFE = ("Kafe", "☕", Colors.LOCATION_CAFE)

    def __init__(self, display_name, emoji, color):
        self.display_name = display_name
        self.emoji = emoji
        self.color = color


# ==================== PERSONAJ KLASSI ====================
class Character:
    """O'yin personaji"""

    def __init__(self, x:  int, y: int):
        self.x = x
        self.y = y
        self.target_x = x
        self. target_y = y
        self.size = 24
        self.speed = 3

        # Animatsiya
        self.direction = "down"  # up, down, left, right
        self.frame = 0
        self.frame_timer = 0
        self.is_moving = False

        # Yo'l bo'ylab harakat
        self.path:  List[Tuple[int, int]] = []
        self.current_path_index = 0
        self.waiting = False
        self.wait_timer = 0

        # Manzilga yetdi
        self.reached_destination = False
        self.celebration_particles:  List[Dict] = []

    def set_path(self, path: List[Tuple[int, int]]):
        """Yo'lni o'rnatish"""
        self.path = path
        self.current_path_index = 0
        self.reached_destination = False
        if path:
            self.x, self.y = path[0]
            self.target_x, self.target_y = path[0]

    def update(self, dt: float):
        """Personajni yangilash"""
        # Kutish vaqti
        if self.waiting:
            self.wait_timer -= dt
            if self.wait_timer <= 0:
                self.waiting = False
                self. current_path_index += 1
            return

        # Yo'l bo'ylab harakat
        if self.path and self.current_path_index < len(self.path):
            target = self.path[self.current_path_index]
            self.target_x, self.target_y = target

            # Yo'nalishni aniqlash
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            dist = math.sqrt(dx * dx + dy * dy)

            if dist < self.speed:
                self.x, self.y = self.target_x, self.target_y
                self.is_moving = False

                # Keyingi nuqtaga o'tish
                if self.current_path_index < len(self.path) - 1:
                    self.waiting = True
                    self.wait_timer = 300  # 300ms kutish
                else:
                    # Manzilga yetdi!
                    self.reached_destination = True
                    self._create_celebration()
            else:
                # Harakat
                self.x += (dx / dist) * self.speed
                self.y += (dy / dist) * self.speed
                self.is_moving = True

                # Yo'nalish
                if abs(dx) > abs(dy):
                    self.direction = "right" if dx > 0 else "left"
                else:
                    self.direction = "down" if dy > 0 else "up"

        # Animatsiya frame
        if self.is_moving:
            self.frame_timer += dt
            if self.frame_timer > 150:
                self.frame = (self.frame + 1) % 4
                self.frame_timer = 0

        # Bayram effekti
        self._update_celebration(dt)

    def _create_celebration(self):
        """Bayram effekti yaratish"""
        for _ in range(50):
            self.celebration_particles.append({
                'x': self.x,
                'y':  self.y,
                'vx': random.uniform(-5, 5),
                'vy': random.uniform(-8, -2),
                'color': random.choice(Colors.CONFETTI),
                'size': random.randint(4, 8),
                'life': 1000
            })

    def _update_celebration(self, dt: float):
        """Bayram effektini yangilash"""
        for p in self.celebration_particles[: ]:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['vy'] += 0.2  # Gravitatsiya
            p['life'] -= dt
            if p['life'] <= 0:
                self.celebration_particles. remove(p)

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        """Personajni chizish"""
        # Tana (doira)
        body_color = (65, 105, 225)  # Royal Blue
        pygame.draw.circle(screen, body_color, (int(self.x), int(self.y)), self.size // 2)

        # Bosh
        head_color = (255, 218, 185)  # Peach
        head_y = int(self.y) - self.size // 2 - 8
        pygame.draw.circle(screen, head_color, (int(self.x), head_y), 10)

        # Ko'zlar
        eye_offset = 3 if self.direction in ["right", "down"] else -3
        pygame.draw.circle(screen, Colors.BLACK, (int(self.x) - 3, head_y - 2), 2)
        pygame.draw.circle(screen, Colors.BLACK, (int(self.x) + 3, head_y - 2), 2)

        # Oyoqlar (animatsiya)
        leg_offset = math.sin(self.frame * math.pi / 2) * 5 if self.is_moving else 0
        pygame.draw.line(screen, Colors.BLACK,
                        (int(self. x) - 5, int(self.y) + self.size // 2 - 5),
                        (int(self.x) - 5 - leg_offset, int(self. y) + self.size // 2 + 8), 3)
        pygame.draw.line(screen, Colors.BLACK,
                        (int(self. x) + 5, int(self.y) + self.size // 2 - 5),
                        (int(self. x) + 5 + leg_offset, int(self.y) + self.size // 2 + 8), 3)

        # Bayram effekti
        for p in self.celebration_particles:
            pygame.draw.circle(screen, p['color'], (int(p['x']), int(p['y'])), p['size'])

        # Manzilga yetganda matn
        if self.reached_destination and len(self.celebration_particles) > 0:
            text = font.render("🎉 YETDI! 🎉", True, Colors. STAR_YELLOW)
            text_rect = text.get_rect(center=(int(self.x), int(self.y) - 50))
            screen.blit(text, text_rect)


# ==================== JOY (NODE) KLASSI ====================
class Location:
    """Xaritadagi joy"""

    def __init__(self, x: int, y: int, loc_type: LocationType):
        self.x = x
        self.y = y
        self. loc_type = loc_type
        self.size = 48

        # Holatlar
        self.is_start = False
        self.is_end = False
        self.is_visited = False
        self. is_current = False
        self.is_path = False
        self.is_hovered = False

        # Dijkstra
        self.distance = float('inf')
        self.previous:  Optional['Location'] = None
        self. previous_road: Optional['Road'] = None

        # Animatsiya
        self. pulse_value = 0
        self.pulse_direction = 1

    def update(self, dt: float):
        """Animatsiyani yangilash"""
        if self.is_current:
            self.pulse_value += self.pulse_direction * dt * 0.01
            if self.pulse_value > 1:
                self.pulse_direction = -1
            elif self.pulse_value < 0:
                self.pulse_direction = 1

    def draw(self, screen: pygame.Surface, font_emoji: pygame.font.Font, font_text: pygame.font.Font):
        """Joyni chizish"""
        # Pulsatsiya o'lchami
        pulse_size = int(self.pulse_value * 10) if self.is_current else 0
        size = self.size + pulse_size

        # Fon rangi
        if self.is_path:
            bg_color = Colors.NODE_PATH
        elif self.is_current:
            bg_color = Colors.NODE_CURRENT
        elif self.is_visited:
            bg_color = Colors.NODE_VISITED
        elif self.is_hovered:
            bg_color = Colors.NODE_HOVER
        else:
            bg_color = self.loc_type.color

        # Asosiy shakl - bino ko'rinishida
        rect = pygame.Rect(self. x - size // 2, self.y - size // 2, size, size)

        # Soya
        shadow_rect = rect.copy()
        shadow_rect.x += 3
        shadow_rect.y += 3
        pygame.draw. rect(screen, Colors.DARK_GRAY, shadow_rect, border_radius=8)

        # Asosiy qism
        pygame.draw.rect(screen, bg_color, rect, border_radius=8)

        # Chegara
        border_color = Colors.NODE_START if self.is_start else (Colors.NODE_END if self. is_end else Colors. DARK_GRAY)
        border_width = 4 if (self.is_start or self. is_end) else 2
        pygame.draw.rect(screen, border_color, rect, border_width, border_radius=8)

        # Emoji
        emoji_text = font_emoji.render(self.loc_type.emoji, True, Colors.BLACK)
        emoji_rect = emoji_text.get_rect(center=(self.x, self.y - 5))
        screen.blit(emoji_text, emoji_rect)

        # Nom (pastda)
        if self.is_hovered or self.is_start or self.is_end:
            name_text = font_text.render(self.loc_type.display_name, True, Colors. DARK_GRAY)
            name_rect = name_text.get_rect(center=(self.x, self.y + size // 2 + 12))

            # Fon
            bg_rect = name_rect.inflate(10, 4)
            pygame.draw.rect(screen, Colors.WHITE, bg_rect, border_radius=3)
            pygame.draw.rect(screen, Colors. GRAY, bg_rect, 1, border_radius=3)
            screen.blit(name_text, name_rect)

        # Start/End belgisi
        if self.is_start:
            flag = font_emoji.render("🚩", True, Colors.NODE_START)
            screen.blit(flag, (self.x + size // 2 - 5, self.y - size // 2 - 10))
        elif self.is_end:
            flag = font_emoji.render("🎯", True, Colors.NODE_END)
            screen.blit(flag, (self.x + size // 2 - 5, self.y - size // 2 - 10))

    def contains_point(self, pos: Tuple[int, int]) -> bool:
        """Nuqta ichida tekshirish"""
        half = self.size // 2
        return (self.x - half <= pos[0] <= self.x + half and
                self.y - half <= pos[1] <= self.y + half)


    def reset_pathfinding(self):
        """Yo'l topish ma'lumotlarini tozalash"""
        self. is_visited = False
        self.is_current = False
        self.is_path = False
        self. distance = float('inf')
        self.previous = None
        self. previous_road = None

    def __lt__(self, other):
        return self.distance < other.distance


# ==================== YO'L (EDGE) KLASSI ====================
class Road:
    """Ikki joy orasidagi yo'l"""

    def __init__(self, loc1: Location, loc2: Location, road_type: RoadType, directed: bool = False):
        self.loc1 = loc1
        self.loc2 = loc2
        self.road_type = road_type
        self. directed = directed
        self.original_weight = road_type.weight
        self.weight = road_type.weight

        # Holatlar
        self.is_visited = False
        self.is_path = False

        # Animatsiya
        self.arrow_offset = 0

    def update(self, dt: float):
        """Animatsiya"""
        if self.directed:
            self.arrow_offset = (self.arrow_offset + dt * 0.1) % 20

    def draw(self, screen: pygame.Surface, font: pygame.font.Font, show_weight: bool = True):
        """Yo'lni chizish"""
        color = Colors.NODE_PATH if self.is_path else (Colors.NODE_VISITED if self.is_visited else self.road_type.color)
        width = self.road_type.width + (2 if self.is_path else 0)

        x1, y1 = self. loc1.x, self.loc1.y
        x2, y2 = self.loc2.x, self.loc2.y

        # Nuqtali chiziq
        if self.road_type.dashed and not self.is_path:
            self._draw_dashed_line(screen, color, (x1, y1), (x2, y2), width)
        else:
            pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)

        # Yo'nalish o'qi
        if self.directed:
            self._draw_arrow(screen, color)

        # Og'irlik
        if show_weight:
            self._draw_weight(screen, font)

    def _draw_dashed_line(self, screen, color, start, end, width):
        """Nuqtali chiziq"""
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1
        dist = math.sqrt(dx * dx + dy * dy)

        if dist == 0:
            return

        dash_len = 10
        gap_len = 5

        dx /= dist
        dy /= dist

        pos = 0
        while pos < dist:
            start_pos = (x1 + dx * pos, y1 + dy * pos)
            end_pos = (x1 + dx * min(pos + dash_len, dist), y1 + dy * min(pos + dash_len, dist))
            pygame.draw.line(screen, color, start_pos, end_pos, width)
            pos += dash_len + gap_len

    def _draw_arrow(self, screen, color):
        """O'q chizish"""
        dx = self.loc2.x - self.loc1.x
        dy = self.loc2.y - self.loc1.y
        length = math.sqrt(dx * dx + dy * dy)

        if length == 0:
            return

        dx /= length
        dy /= length

        # O'q pozitsiyasi
        arrow_x = self.loc2.x - dx * (self.loc2.size // 2 + 10)
        arrow_y = self.loc2.y - dy * (self.loc2.size // 2 + 10)

        # O'q boshi
        arrow_size = 12
        angle = math.pi / 6

        left_x = arrow_x - arrow_size * (dx * math.cos(angle) + dy * math.sin(angle))
        left_y = arrow_y - arrow_size * (dy * math.cos(angle) - dx * math.sin(angle))

        right_x = arrow_x - arrow_size * (dx * math.cos(angle) - dy * math.sin(angle))
        right_y = arrow_y - arrow_size * (dy * math.cos(angle) + dx * math.sin(angle))

        pygame.draw.polygon(screen, color, [(arrow_x, arrow_y), (left_x, left_y), (right_x, right_y)])

    def _draw_weight(self, screen, font):
        """Og'irlikni chizish"""
        mid_x = (self.loc1.x + self.loc2.x) // 2
        mid_y = (self.loc1.y + self.loc2.y) // 2

        # Fon
        bg_color = Colors.WHITE if not self.is_path else Colors. NODE_PATH
        pygame.draw.circle(screen, bg_color, (mid_x, mid_y), 14)
        pygame.draw.circle(screen, self.road_type.color, (mid_x, mid_y), 14, 2)

        # Raqam
        text = font. render(str(self.weight), True, Colors. DARK_GRAY)
        text_rect = text.get_rect(center=(mid_x, mid_y))
        screen.blit(text, text_rect)

    def reset_pathfinding(self):
        """Tozalash"""
        self. is_visited = False
        self.is_path = False


# ==================== GRAF KLASSI ====================
class CityMap:
    """Shahar xaritasi (Graf)"""

    def __init__(self):
        self.locations: List[Location] = []
        self.roads: List[Road] = []
        self.directed = False
        self.weighted = True
        self.start_location:  Optional[Location] = None
        self.end_location: Optional[Location] = None

    def add_location(self, x: int, y: int, loc_type: LocationType) -> Location:
        """Joy qo'shish"""
        loc = Location(x, y, loc_type)
        self.locations.append(loc)
        return loc

    def add_road(self, loc1: Location, loc2: Location, road_type: RoadType) -> Optional[Road]:
        """Yo'l qo'shish"""
        # Mavjud yo'lni tekshirish
        for road in self.roads:
            if (road.loc1 == loc1 and road.loc2 == loc2) or \
               (not self.directed and road.loc1 == loc2 and road.loc2 == loc1):
                return None

        road = Road(loc1, loc2, road_type, self.directed)
        if not self.weighted:
            road.weight = 1
        self.roads.append(road)
        return road

    def remove_location(self, loc: Location):
        """Joyni o'chirish"""
        self.roads = [r for r in self. roads if r.loc1 != loc and r.loc2 != loc]
        if loc in self.locations:
            self.locations.remove(loc)
        if self.start_location == loc:
            self.start_location = None
        if self.end_location == loc:
            self.end_location = None

    def remove_road(self, road: Road):
        """Yo'lni o'chirish"""
        if road in self.roads:
            self.roads.remove(road)

    def get_neighbors(self, loc: Location) -> List[Tuple[Location, Road, int]]:
        """Qo'shnilarni olish"""
        neighbors = []
        for road in self.roads:
            if road.loc1 == loc:
                neighbors.append((road.loc2, road, road.weight))
            elif not self.directed and road.loc2 == loc:
                neighbors. append((road.loc1, road, road.weight))
        return neighbors

    def get_location_at(self, pos: Tuple[int, int]) -> Optional[Location]:
        """Pozitsiyadagi joy"""
        for loc in self.locations:
            if loc.contains_point(pos):
                return loc
        return None

    def get_road_at(self, pos: Tuple[int, int], threshold: int = 15) -> Optional[Road]:
        """Pozitsiyadagi yo'l"""
        px, py = pos
        for road in self.roads:
            x1, y1 = road.loc1.x, road.loc1.y
            x2, y2 = road.loc2.x, road. loc2.y

            line_len = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if line_len == 0:
                continue

            dist = abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1) / line_len
            dot = ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / (line_len ** 2)

            if 0 <= dot <= 1 and dist <= threshold:
                return road
        return None

    def set_directed(self, directed: bool):
        """Yo'nalishli/yo'nalishsiz"""
        self.directed = directed
        for road in self.roads:
            road.directed = directed

    def set_weighted(self, weighted: bool):
        """Og'irlikli/og'irliksiz"""
        self.weighted = weighted
        for road in self.roads:
            if weighted:
                road.weight = road.original_weight
            else:
                road.weight = 1

    def set_start(self, loc: Location):
        """Boshlang'ich joy"""
        if self.start_location:
            self.start_location.is_start = False
        loc.is_start = True
        self.start_location = loc

    def set_end(self, loc: Location):
        """Yakuniy joy"""
        if self.end_location:
            self.end_location.is_end = False
        loc.is_end = True
        self.end_location = loc

    def reset_pathfinding(self):
        """Yo'l topishni tozalash"""
        for loc in self.locations:
            loc.reset_pathfinding()
        for road in self.roads:
            road.reset_pathfinding()

    def clear(self):
        """Hammasini tozalash"""
        self.locations.clear()
        self.roads.clear()
        self.start_location = None
        self.end_location = None

    def update(self, dt: float):
        """Yangilash"""
        for loc in self.locations:
            loc. update(dt)
        for road in self.roads:
            road.update(dt)

    def draw(self, screen:  pygame.Surface, font_emoji: pygame.font.Font,
             font_text: pygame. font.Font, font_weight: pygame.font.Font):
        """Chizish"""
        # Avval yo'llar
        for road in self.roads:
            road.draw(screen, font_weight, self.weighted)

        # Keyin joylar
        for loc in self.locations:
            loc.draw(screen, font_emoji, font_text)


# ==================== DIJKSTRA ALGORITMI ====================
class DijkstraPathfinder:
    """Dijkstra algoritmi"""

    def __init__(self, city_map: CityMap):
        self.city_map = city_map
        self.is_running = False
        self.is_finished = False
        self. path_found = False
        self.path_weight = 0
        self.path_nodes:  List[Location] = []
        self.execution_time = 0.0
        self.animation_speed = 400

        self.priority_queue:  List[Tuple[float, Location]] = []
        self.visited:  set = set()
        self.start_time = 0.0

    def start(self) -> bool:
        """Boshlash"""
        if not self.city_map.start_location or not self.city_map.end_location:
            return False

        self.city_map.reset_pathfinding()

        self.is_running = True
        self. is_finished = False
        self.path_found = False
        self.path_weight = 0
        self.path_nodes = []
        self.visited = set()
        self.start_time = time.time()

        self.city_map.start_location.distance = 0
        self.priority_queue = [(0, self. city_map.start_location)]

        return True

    def step(self) -> bool:
        """Bir qadam"""
        if not self. is_running or not self.priority_queue:
            self.is_running = False
            self.is_finished = True
            self.execution_time = (time.time() - self.start_time) * 1000
            return False

        current_dist, current = heapq.heappop(self.priority_queue)

        if current in self.visited:
            return True

        self.visited. add(current)

        # Oldingi nuqtani yangilash
        for loc in self.city_map.locations:
            if loc.is_current and loc != self.city_map.start_location and loc != self.city_map.end_location:
                loc.is_current = False
                loc.is_visited = True

        if current != self.city_map.start_location and current != self.city_map.end_location:
            current.is_current = True

        # Manzilga yetdik
        if current == self.city_map. end_location:
            self. is_running = False
            self.is_finished = True
            self.path_found = True
            self. execution_time = (time.time() - self.start_time) * 1000
            self._reconstruct_path()
            return False

        # Qo'shnilar
        for neighbor, road, weight in self.city_map.get_neighbors(current):
            if neighbor not in self.visited:
                new_dist = current. distance + weight

                if new_dist < neighbor. distance:
                    neighbor.distance = new_dist
                    neighbor.previous = current
                    neighbor.previous_road = road
                    heapq.heappush(self.priority_queue, (new_dist, neighbor))
                    road.is_visited = True

        return True

    def _reconstruct_path(self):
        """Yo'lni qayta qurish"""
        self.path_nodes = []
        current = self.city_map. end_location

        while current:
            self.path_nodes. append(current)

            if current != self.city_map.start_location and current != self.city_map. end_location:
                current. is_path = True
                current.is_visited = False
                current.is_current = False

            if current. previous_road:
                current.previous_road.is_path = True
                current.previous_road. is_visited = False

            current = current.previous

        self.path_nodes. reverse()
        self.path_weight = int(self.city_map.end_location.distance)

    def get_path_coordinates(self) -> List[Tuple[int, int]]:
        """Yo'l koordinatalari"""
        return [(loc.x, loc.y) for loc in self.path_nodes]

    def reset(self):
        """Qayta boshlash"""
        self.is_running = False
        self.is_finished = False
        self.path_found = False
        self.path_weight = 0
        self.path_nodes = []
        self.priority_queue = []
        self. visited = set()


# ==================== UI TUGMALARI ====================
class Button:
    """Tugma"""

    def __init__(self, x: int, y: int, width: int, height: int,
                 text: str, color:  Tuple[int, int, int], icon: str = ""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.icon = icon
        self.color = color
        self.hover_color = tuple(max(0, c - 30) for c in color)
        self.is_hovered = False
        self.is_active = False

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        """Chizish"""
        color = self.hover_color if self.is_hovered else self.color

        # Aktiv tugma
        if self. is_active:
            pygame. draw.rect(screen, Colors.WHITE, self.rect. inflate(4, 4), border_radius=8)

        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        pygame.draw.rect(screen, Colors. DARK_GRAY, self.rect, 2, border_radius=6)

        # Matn
        display_text = f"{self.icon} {self.text}" if self.icon else self.text
        text_surface = font. render(display_text, True, Colors.TEXT_WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos: Tuple[int, int]):
        self.is_hovered = self. rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)


class ToggleButton:
    """Toggle tugma"""

    def __init__(self, x: int, y: int, width: int, height: int,
                 text_on: str, text_off: str, icon_on: str, icon_off: str,
                 color_on:  Tuple[int, int, int], color_off: Tuple[int, int, int], is_on: bool = False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text_on = text_on
        self.text_off = text_off
        self.icon_on = icon_on
        self.icon_off = icon_off
        self.color_on = color_on
        self.color_off = color_off
        self.is_on = is_on
        self.is_hovered = False

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        color = self.color_on if self.is_on else self.color_off
        if self.is_hovered:
            color = tuple(max(0, c - 20) for c in color)

        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        pygame.draw.rect(screen, Colors. DARK_GRAY, self.rect, 2, border_radius=6)

        icon = self.icon_on if self.is_on else self.icon_off
        text = self.text_on if self.is_on else self.text_off
        display_text = f"{icon} {text}"

        text_surface = font.render(display_text, True, Colors.TEXT_WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos:  Tuple[int, int]):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def toggle(self):
        self.is_on = not self.is_on

    def is_clicked(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)


# ==================== POPUP MENU ====================
class PopupMenu:
    """Tanlash menyusi"""

    def __init__(self):
        self.visible = False
        self.x = 0
        self.y = 0
        self.items:  List[Tuple[str, str, any]] = []  # (icon, text, value)
        self.item_height = 35
        self.width = 160
        self.selected_index = -1

    def show(self, x: int, y: int, items: List[Tuple[str, str, any]]):
        """Ko'rsatish"""
        self.x = x
        self.y = y
        self.items = items
        self.visible = True
        self.selected_index = -1

    def hide(self):
        """Yashirish"""
        self.visible = False
        self.items = []

    def update(self, mouse_pos: Tuple[int, int]):
        """Yangilash"""
        if not self.visible:
            return

        mx, my = mouse_pos
        if self.x <= mx <= self.x + self.width:
            index = (my - self.y) // self.item_height
            if 0 <= index < len(self.items):
                self.selected_index = index
            else:
                self.selected_index = -1
        else:
            self.selected_index = -1

    def get_clicked_item(self, mouse_pos: Tuple[int, int]) -> Optional[any]:
        """Bosilgan element"""
        if not self.visible:
            return None

        mx, my = mouse_pos
        if self.x <= mx <= self.x + self.width:
            index = (my - self.y) // self.item_height
            if 0 <= index < len(self.items):
                self.hide()
                return self.items[index][2]

        self.hide()
        return None

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        """Chizish"""
        if not self.visible:
            return

        height = len(self.items) * self.item_height
        rect = pygame.Rect(self.x, self.y, self.width, height)

        # Soya
        shadow = rect.copy()
        shadow.x += 3
        shadow.y += 3
        pygame.draw.rect(screen, Colors.DARK_GRAY, shadow, border_radius=8)

        # Fon
        pygame.draw.rect(screen, Colors.WHITE, rect, border_radius=8)
        pygame.draw.rect(screen, Colors. GRAY, rect, 2, border_radius=8)

        # Elementlar
        for i, (icon, text, _) in enumerate(self.items):
            item_rect = pygame.Rect(self.x, self.y + i * self. item_height, self.width, self.item_height)

            if i == self.selected_index:
                pygame.draw.rect(screen, Colors.NODE_HOVER, item_rect)

            display_text = f"{icon} {text}"
            text_surface = font.render(display_text, True, Colors. DARK_GRAY)
            text_rect = text_surface.get_rect(midleft=(self.x + 10, item_rect.centery))
            screen.blit(text_surface, text_rect)


# ==================== ASOSIY O'YIN ====================
class DijkstraAdventure:
    """Asosiy o'yin klassi"""

    def __init__(self):
        pygame.init()

        # O'lchamlar
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.UI_HEIGHT = 130
        self.FPS = 60

        # Ekran
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("🎮 Dijkstra Sarguzasht O'yini")

        # Shriftlar
        self.font_small = pygame.font.SysFont('Segoe UI Emoji', 12)
        self.font_medium = pygame.font.SysFont('Segoe UI Emoji', 14)
        self.font_large = pygame.font.SysFont('Segoe UI Emoji', 18)
        self.font_emoji = pygame.font.SysFont('Segoe UI Emoji', 24)
        self.font_title = pygame.font.SysFont('Segoe UI Emoji', 20, bold=True)

        # O'yin elementlari
        self.city_map = CityMap()
        self.pathfinder = DijkstraPathfinder(self.city_map)
        self.character = Character(100, 300)

        # UI
        self._create_ui()
        self. popup = PopupMenu()

        # Holatlar
        self.clock = pygame.time.Clock()
        self.running = True
        self.mode = "location"  # location, road, start, end, delete

        # Yo'l chizish
        self.road_start:  Optional[Location] = None
        self.selected_road_type = RoadType.HIGHWAY
        self.selected_loc_type = LocationType.HOME

        # Animatsiya
        self.algorithm_running = False
        self.character_moving = False
        self. last_step_time = 0

        # Tezlik
        self.speed_levels = [800, 400, 200, 100, 50]
        self.speed_names = ["Juda sekin", "Sekin", "Normal", "Tez", "Juda tez"]
        self.current_speed = 2

    def _create_ui(self):
        """UI yaratish"""
        btn_h = 32
        row1_y = 10
        row2_y = 48
        row3_y = 86

        # Rejim tugmalari
        self.buttons = {
            "mode_location": Button(10, row1_y, 90, btn_h, "Joy", Colors.BUTTON_BLUE, "🏠"),
            "mode_road": Button(105, row1_y, 90, btn_h, "Yo'l", Colors.BUTTON_BLUE, "🛤️"),
            "mode_start": Button(200, row1_y, 100, btn_h, "Boshlash", Colors.BUTTON_GREEN, "🚩"),
            "mode_end":  Button(305, row1_y, 100, btn_h, "Manzil", Colors.BUTTON_RED, "🎯"),
            "mode_delete": Button(410, row1_y, 90, btn_h, "O'chirish", Colors.BUTTON_ORANGE, "🗑️"),

            # Amallar
            "run":  Button(10, row2_y, 100, btn_h, "BOSHLASH", Colors.BUTTON_GREEN, "▶️"),
            "clear_path": Button(115, row2_y, 110, btn_h, "Yo'l o'chir", Colors.BUTTON_ORANGE, "🔄"),
            "clear_all": Button(230, row2_y, 100, btn_h, "Tozalash", Colors.BUTTON_RED, "🗑️"),
            "example": Button(335, row2_y, 90, btn_h, "Namuna", Colors.BUTTON_PURPLE, "📋"),

            # Tezlik
            "speed_down": Button(560, row2_y, 35, btn_h, "-", Colors.BUTTON_BLUE),
            "speed_up": Button(710, row2_y, 35, btn_h, "+", Colors.BUTTON_BLUE),
        }

        # Toggle tugmalari
        self.toggles = {
            "directed": ToggleButton(520, row1_y, 140, btn_h,
                                     "Yo'nalishli", "Yo'nalishsiz", "➡️", "↔️",
                                     Colors.BUTTON_GREEN, Colors.BUTTON_BLUE, False),
            "weighted": ToggleButton(665, row1_y, 140, btn_h,
                                     "Og'irlikli", "Og'irliksiz", "⚖️", "1️⃣",
                                     Colors.BUTTON_ORANGE, Colors.BUTTON_PURPLE, True),
        }

    def handle_events(self):
        """Voqealar"""
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self. running = False

            elif event.type == pygame. KEYDOWN:
                self._handle_keydown(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_down(event, mouse_pos)

            elif event.type == pygame. MOUSEBUTTONUP:
                self._handle_mouse_up(event, mouse_pos)

        self._update_hover(mouse_pos)

    def _handle_keydown(self, event):
        """Klaviatura"""
        key_map = {
            pygame.K_1: lambda: setattr(self, 'mode', 'location'),
            pygame.K_2: lambda: setattr(self, 'mode', 'road'),
            pygame.K_3: lambda: setattr(self, 'mode', 'start'),
            pygame.K_4: lambda: setattr(self, 'mode', 'end'),
            pygame.K_5: lambda: setattr(self, 'mode', 'delete'),
            pygame.K_SPACE: self._start_pathfinding,
            pygame.K_c: self._clear_all,
            pygame.K_r: self._clear_path,
            pygame.K_e: self._create_example,
            pygame.K_d: lambda: (self.toggles["directed"].toggle(),
                                 self.city_map.set_directed(self.toggles["directed"].is_on)),
            pygame.K_w: lambda: (self.toggles["weighted"].toggle(),
                                 self.city_map. set_weighted(self.toggles["weighted"].is_on)),
        }

        action = key_map.get(event.key)
        if action:
            action()

    def _handle_mouse_down(self, event, pos):
        """Sichqoncha bosish"""
        # Popup ochiq bo'lsa
        if self.popup.visible:
            result = self.popup.get_clicked_item(pos)
            if result:
                if isinstance(result, LocationType):
                    self.selected_loc_type = result
                elif isinstance(result, RoadType):
                    self.selected_road_type = result
                    if self.road_start:
                        # Yo'l qo'shish
                        loc = self.city_map.get_location_at(pos)
                        if loc and loc != self.road_start:
                            self.city_map.add_road(self.road_start, loc, self.selected_road_type)
                        self.road_start = None
            return

        # UI tugmalari
        if pos[1] < self.UI_HEIGHT:
            self._handle_ui_click(pos)
            return

        # Canvas
        if event.button == 1:
            self._handle_canvas_click(pos)
        elif event.button == 3:
            self._handle_right_click(pos)

    def _handle_mouse_up(self, event, pos):
        """Sichqoncha qo'yish"""
        if self.road_start and self.mode == "road":
            loc = self.city_map.get_location_at(pos)
            if loc and loc != self.road_start:
                # Yo'l turi tanlash popup
                items = [(rt.value[0][: 15], rt.value[0], rt) for rt in RoadType]
                self.popup.show(pos[0], pos[1], items)
                self._temp_road_end = loc
            else:
                self. road_start = None

    def _handle_ui_click(self, pos):
        """UI bosish"""
        mode_map = {
            "mode_location": "location",
            "mode_road":  "road",
            "mode_start": "start",
            "mode_end": "end",
            "mode_delete": "delete",
        }

        for name, mode in mode_map.items():
            if self.buttons[name]. is_clicked(pos):
                self.mode = mode
                return

        if self.buttons["run"].is_clicked(pos):
            self._start_pathfinding()
        elif self.buttons["clear_path"]. is_clicked(pos):
            self._clear_path()
        elif self.buttons["clear_all"].is_clicked(pos):
            self._clear_all()
        elif self.buttons["example"]. is_clicked(pos):
            self._create_example()
        elif self.buttons["speed_down"].is_clicked(pos):
            self._change_speed(-1)
        elif self.buttons["speed_up"].is_clicked(pos):
            self._change_speed(1)

        if self.toggles["directed"].is_clicked(pos):
            self.toggles["directed"].toggle()
            self.city_map.set_directed(self.toggles["directed"].is_on)
        elif self.toggles["weighted"].is_clicked(pos):
            self.toggles["weighted"].toggle()
            self.city_map. set_weighted(self.toggles["weighted"].is_on)

    def _handle_canvas_click(self, pos):
        """Canvas bosish"""
        loc = self.city_map.get_location_at(pos)
        road = self.city_map.get_road_at(pos)

        if self.mode == "location":
            if not loc:
                # Joy turi popup
                items = [(lt.emoji, lt.display_name, lt) for lt in LocationType]
                self.popup.show(pos[0], pos[1], items)
                self._pending_location_pos = pos

        elif self.mode == "road":
            if loc:
                self.road_start = loc

        elif self.mode == "start":
            if loc:
                self.city_map.set_start(loc)
                self.character.x = loc.x
                self. character.y = loc.y

        elif self.mode == "end":
            if loc:
                self.city_map.set_end(loc)

        elif self.mode == "delete":
            if loc:
                self.city_map.remove_location(loc)
            elif road:
                self.city_map.remove_road(road)

    def _handle_right_click(self, pos):
        """O'ng tugma - o'chirish"""
        loc = self.city_map.get_location_at(pos)
        road = self.city_map.get_road_at(pos)

        if loc:
            self.city_map.remove_location(loc)
        elif road:
            self.city_map.remove_road(road)

    def _update_hover(self, pos):
        """Hover yangilash"""
        for btn in self.buttons.values():
            btn.update(pos)
        for toggle in self.toggles.values():
            toggle.update(pos)
        self.popup.update(pos)

        for loc in self.city_map.locations:
            loc. is_hovered = loc. contains_point(pos) and pos[1] > self.UI_HEIGHT

        # Aktiv tugmani belgilash
        mode_buttons = {
            "location": "mode_location",
            "road":  "mode_road",
            "start": "mode_start",
            "end": "mode_end",
            "delete": "mode_delete"
        }
        for mode, btn_name in mode_buttons.items():
            self.buttons[btn_name].is_active = (self.mode == mode)

    def _change_speed(self, direction):
        """Tezlik o'zgartirish"""
        self.current_speed = max(0, min(len(self.speed_levels) - 1, self.current_speed + direction))
        self.pathfinder.animation_speed = self.speed_levels[self.current_speed]

    def _start_pathfinding(self):
        """Yo'l topishni boshlash"""
        if self.algorithm_running or self.character_moving:
            return

        self._clear_path()
        self.character. reached_destination = False
        self.character. celebration_particles = []

        if self.pathfinder.start():
            self.algorithm_running = True
            self.last_step_time = pygame.time.get_ticks()

    def _clear_path(self):
        """Yo'lni tozalash"""
        self.city_map.reset_pathfinding()
        self.pathfinder.reset()
        self.algorithm_running = False
        self. character_moving = False
        self.character.path = []
        self.character. reached_destination = False
        self.character.celebration_particles = []

    def _clear_all(self):
        """Hammasini tozalash"""
        self.city_map.clear()
        self.pathfinder.reset()
        self.algorithm_running = False
        self.character_moving = False
        self.character.path = []
        self. character.x = 100
        self.character.y = 300

    def _create_example(self):
        """Namuna xarita"""
        self._clear_all()

        # Joylar
        locations = [
            (150, 250, LocationType.HOME),
            (350, 180, LocationType.CAFE),
            (550, 200, LocationType.SHOP),
            (200, 450, LocationType.PARK),
            (400, 400, LocationType.SCHOOL),
            (600, 450, LocationType.HOSPITAL),
            (750, 300, LocationType.CAFE),
            (900, 400, LocationType.SHOP),
        ]

        locs = []
        for x, y, lt in locations:
            locs. append(self.city_map.add_location(x, y + self.UI_HEIGHT, lt))

        # Yo'llar
        roads = [
            (0, 1, RoadType.HIGHWAY),
            (1, 2, RoadType.BIKE),
            (0, 3, RoadType. WALK),
            (1, 4, RoadType.MOUNTAIN),
            (2, 5, RoadType.BRIDGE),
            (3, 4, RoadType.HIGHWAY),
            (4, 5, RoadType.BIKE),
            (2, 6, RoadType. TUNNEL),
            (5, 7, RoadType.HIGHWAY),
            (6, 7, RoadType.WALK),
            (4, 6, RoadType.MOUNTAIN),
        ]

        for i, j, rt in roads:
            self.city_map.add_road(locs[i], locs[j], rt)

        # Start va End
        self.city_map. set_start(locs[0])
        self.city_map.set_end(locs[7])

        self.character.x = locs[0].x
        self.character.y = locs[0].y

    def update(self):
        """Yangilash"""
        dt = self.clock.get_time()

        # Algoritm animatsiyasi
        if self. algorithm_running:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_step_time >= self.pathfinder.animation_speed:
                if not self.pathfinder.step():
                    self.algorithm_running = False
                    if self.pathfinder.path_found:
                        # Personajni harakatga tushirish
                        self.character.set_path(self.pathfinder.get_path_coordinates())
                        self.character_moving = True
                self.last_step_time = current_time

        # Personaj harakati
        if self.character_moving:
            self.character.update(dt)
            if self.character.reached_destination:
                self.character_moving = False

        # Bayram effekti yangilash
        if self.character.reached_destination:
            self.character.update(dt)

        # Xarita animatsiyalari
        self. city_map.update(dt)

        # Popup - joy qo'shish
        if hasattr(self, '_pending_location_pos') and self.popup.visible == False:
            if hasattr(self, 'selected_loc_type'):
                self.city_map.add_location(self._pending_location_pos[0],
                                           self._pending_location_pos[1],
                                           self.selected_loc_type)
            delattr(self, '_pending_location_pos')

        # Popup - yo'l qo'shish
        if hasattr(self, '_temp_road_end') and self.popup.visible == False:
            if self.road_start and hasattr(self, 'selected_road_type'):
                self.city_map.add_road(self. road_start, self._temp_road_end, self.selected_road_type)
            self. road_start = None
            delattr(self, '_temp_road_end')

    def draw(self):
        """Chizish"""
        # Fon
        self.screen.fill(Colors. CANVAS_BG)

        # Grid
        for x in range(0, self.WIDTH, 50):
            pygame.draw.line(self.screen, Colors. GRID_LINE, (x, self.UI_HEIGHT), (x, self.HEIGHT))
        for y in range(self.UI_HEIGHT, self.HEIGHT, 50):
            pygame.draw. line(self.screen, Colors. GRID_LINE, (0, y), (self.WIDTH, y))

        # Xarita
        self.city_map.draw(self.screen, self.font_emoji, self.font_medium, self.font_medium)

        # Yo'l chizish jarayonida
        if self.road_start:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(self.screen, Colors.BUTTON_BLUE,
                           (self.road_start.x, self.road_start.y), mouse_pos, 3)

        # Personaj
        self.character.draw(self.screen, self.font_large)

        # Popup
        self.popup.draw(self.screen, self.font_medium)

        # UI
        self._draw_ui()

        pygame.display.flip()

        def draw(self):
            """Chizish"""
            # Fon
            self.screen.fill(Colors.CANVAS_BG)

            # Grid
            for x in range(0, self.WIDTH, 50):
                pygame.draw.line(self.screen, Colors.GRID_LINE, (x, self.UI_HEIGHT), (x, self.HEIGHT))
            for y in range(self.UI_HEIGHT, self.HEIGHT, 50):
                pygame.draw.line(self.screen, Colors.GRID_LINE, (0, y), (self.WIDTH, y))

            # Xarita
            self.city_map.draw(self.screen, self.font_emoji, self.font_medium, self.font_medium)

            # Yo'l chizish jarayonida
            if self.road_start:
                mouse_pos = pygame.mouse.get_pos()
                pygame.draw.line(self.screen, Colors.BUTTON_BLUE,
                                 (self.road_start.x, self.road_start.y), mouse_pos, 3)

            # Personaj
            self.character.draw(self.screen, self.font_large)

            # Popup
            self.popup.draw(self.screen, self.font_medium)

            # UI
            self._draw_ui()

            pygame.display.flip()

        def _draw_ui(self):
            """UI chizish"""
            # Panel foni
            pygame.draw.rect(self.screen, Colors.PANEL_BG, (0, 0, self.WIDTH, self.UI_HEIGHT))
            pygame.draw.rect(self.screen, Colors.PANEL_LIGHT, (0, self.UI_HEIGHT - 4, self.WIDTH, 4))

            # Tugmalar
            for btn in self.buttons.values():
                btn.draw(self.screen, self.font_medium)

            # Toggle
            for toggle in self.toggles.values():
                toggle.draw(self.screen, self.font_medium)

            # Tezlik ko'rsatkich
            speed_rect = pygame.Rect(600, 48, 105, 32)
            pygame.draw.rect(self.screen, Colors.DARK_GRAY, speed_rect, border_radius=5)
            speed_text = self.font_medium.render(self.speed_names[self.current_speed], True, Colors.TEXT_WHITE)
            self.screen.blit(speed_text, speed_text.get_rect(center=speed_rect.center))

            # Ma'lumotlar paneli (o'ng tomon)
            info_x = 820
            info_y = 10

            # FPS
            fps_text = f"FPS: {int(self.clock.get_fps())}"
            self.screen.blit(self.font_medium.render(fps_text, True, Colors.TEXT_WHITE), (info_x, info_y))

            # Statistika
            stats_text = f"Joylar:  {len(self.city_map.locations)}   Yo'llar: {len(self.city_map.roads)}"
            self.screen.blit(self.font_medium.render(stats_text, True, Colors.TEXT_WHITE), (info_x, info_y + 22))

            # Boshlang'ich va yakuniy
            start_name = self.city_map.start_location.loc_type.display_name if self.city_map.start_location else "---"
            end_name = self.city_map.end_location.loc_type.display_name if self.city_map.end_location else "---"
            route_text = f"{start_name} -> {end_name}"
            self.screen.blit(self.font_medium.render(route_text, True, Colors.TEXT_WHITE), (info_x, info_y + 44))

            # Natija
            if self.pathfinder.path_found:
                result_color = Colors.NODE_PATH
                result_text = f"Yo'l topildi!  Masofa: {self.pathfinder.path_weight}"
                self.screen.blit(self.font_large.render(result_text, True, result_color), (info_x, info_y + 70))

                time_text = f"Vaqt: {self.pathfinder.execution_time:. 1f}ms"
                self.screen.blit(self.font_medium.render(time_text, True, Colors.TEXT_WHITE), (info_x, info_y + 95))
            elif self.pathfinder.is_finished and not self.pathfinder.path_found:
                self.screen.blit(self.font_large.render("Yo'l topilmadi!", True, Colors.BUTTON_RED),
                                 (info_x, info_y + 70))

            # Joriy rejim
            mode_names = {
                "location": "Joy qo'shish",
                "road": "Yo'l chizish",
                "start": "Boshlang'ich",
                "end": "Manzil",
                "delete": "O'chirish"
            }
            mode_text = f"Rejim: {mode_names.get(self.mode, self.mode)}"
            self.screen.blit(self.font_title.render(mode_text, True, Colors.NODE_PATH), (info_x + 150, info_y))

            # Yordam (pastda)
            help_y = 108
            help_text = "[1-5] Rejim  [SPACE] Boshlash  [D] Yo'nalish  [W] Og'irlik  [E] Namuna  [C] Tozalash"
            self.screen.blit(self.font_small.render(help_text, True, Colors.GRAY), (10, help_y))

        def run(self):
            """Asosiy sikl"""
            print("=" * 70)
            print("DIJKSTRA SARGUZASHT O'YINI")
            print("=" * 70)
            print("\nBOSHQARUV:")
            print("  [1] Joy qo'shish rejimi")
            print("  [2] Yo'l chizish rejimi")
            print("  [3] Boshlang'ich nuqta")
            print("  [4] Manzil")
            print("  [5] O'chirish rejimi")
            print("  [SPACE] Algoritmni boshlash")
            print("  [D] Directed/Undirected")
            print("  [W] Weighted/Unweighted")
            print("  [E] Namuna xarita")
            print("  [C] Hammasini tozalash")
            print("  [R] Yo'lni tozalash")
            print("=" * 70)

            while self.running:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(self.FPS)

            pygame.quit()

    # ==================== ISHGA TUSHIRISH ====================
    if __name__ == "__main__":
        game = DijkstraAdventure()
        game.run()