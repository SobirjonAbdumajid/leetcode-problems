def inorderTraversal(root):
    natija = []
    
    def traverse(node):
        if not node: # Agar tugun bo'sh bo'lsa, to'xta
            return
        
        traverse(node.left)   # 1. Chapga boramiz
        natija.append(node.val) # 2. O'zini yozib olamiz
        traverse(node.right)  # 3. O'ngga boramiz
        
    traverse(root)
    return natija



# Bu funksiya berilgan ikkilik daraxtning inorder (o'rta tartibdagi) sayohatini amalga oshiradi va natijani ro'yxat shaklida qaytaradi.
# Misol uchun, agar daraxt quyidagicha bo'lsa:
#       1
#        \
#         2
#        /
#       3
# Funksiya [1, 3, 2] ni qaytaradi.
# Bu yerda rekursiv yordamchi funksiya `traverse` ishlatiladi, u har bir tugunni tekshiradi va kerakli tartibda qiymatlarni yig'adi.
# Funksiyaning murakkabligi O(n), bu yerda n - daraxtdagi tugunlar soni, chunki har bir tugun bir marta ko'rib chiqiladi.
# Bo'sh joy murakkabligi O(h), bu yerda h - daraxtning balandligi, chunki rekursiv chaqiruvlar stekda saqlanadi.
# Misol uchun foydalanish:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# print(inorderTraversal(root))  # Natija: [1, 3, 2]
# Qo'shimcha eslatma: Bu kod Python dasturlash tilida yozilgan va ikkilik daraxtlar bilan ishlash uchun mo'ljallangan.
# Agar siz boshqa dasturlash tillarida yoki qo'shimcha funksiyalar bilan ishlashni xohlasangiz, iltimos, bildiring.
# Qo'shimcha eslatma: Bu kod Python dasturlash tilida yozilgan va ikkilik daraxtlar bilan ishlash uchun mo'ljallangan.
# Agar siz boshqa dasturlash tillarida yoki qo'shimcha funksiyalar bilan ishlashni xohlasangiz, iltimos, bildiring.
# Qo'shimcha eslatma: Bu kod Python dasturlash tilida yozilgan va ikkilik daraxtlar bilan ishlash uchun mo'ljallangan.
# Agar siz boshqa dasturlash tillarida yoki qo'shimcha funksiyalar bilan ishlishni xohlasangiz, iltimos, bildiring.