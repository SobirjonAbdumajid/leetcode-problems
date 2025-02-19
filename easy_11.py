class Solution(object):
    def maxNumberOfBalloons(self, text):
        total_text_count = 0
        total_balloon_count = 0

        balloon = "balloon"
        for i in "balon":
            total_text_count += text.count(i)
            total_balloon_count += balloon.count(i)
            print(i, total_text_count, total_balloon_count)

        # return total_text_count // total_balloon_count
            # if True:
            # print(i, text.count(i), balloon.count(i))
        # return 0


        # list_text = list(text)
        # counter = 0
        # balloon = "balloon"
        # for i in balloon:
        #     for j in text:
        #         if i == j:
        #             counter += 1
        #             print(counter)
        #             # try:
        #             list_text.remove(j)
        #             # except:
        #             #     counter -= 1
        # return counter // len(balloon)


s = Solution()
print(s.maxNumberOfBalloons("loonbalxballllllllpoon"))

