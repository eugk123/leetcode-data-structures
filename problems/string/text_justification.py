"""

"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        didn't complete. couldn't figure out how to set spaces between words
        
        """
        def buildSpaces(remaining_spaces: int) -> int:
            return remaining_spaces * ' '
        # split the input into each line
        # last line is left justified
        
        sentences = []
        sentence = []
        remaining_spaces = []
        prev_sentence = ""
        count_wo_space = count_w_space = 0
        for word in words:
            # this count is the char count per line
            # we do a +1 for space
            count_w_space = count_w_space + 1 + len(word)
            count_wo_space = count_wo_space + len(word)
            sentence.append(word)
            
            # we use +1 on maxWidth, 
            # because if n_words = 2, we get " word1 word2", we have an extra space in the far left.
            if count_w_space > maxWidth + 1:
                # trim last word off and append sentence
                sentence.pop()
                sentences.append(sentence)
                
                # append total count w/o space, need to trim off last word
                count_wo_space = count_wo_space - len(word)
                remaining_spaces.append(maxWidth - count_wo_space)
                
                # next sentence setup. reset counter and set next sentence to word.
                count_w_space, count_wo_space, sentence = 1 + len(word), len(word), [word]
                
        # make sure to append last iteration
        remaining_spaces.append(maxWidth - count_wo_space)
        sentences.append(sentence)
        print(sentences)
        print(remaining_spaces)

        result = []  # appending of all result sentences
        result_sentence = ""
        
        # equal spaces between each word
        for i in range(len(sentences)-1):
            sentence, remaining_space = sentences[i], remaining_spaces[i]
            
            
            # do some math, figure out how many spaces between each word
            last_space_minus_one = last_space_plus_one = False
            
            if len(sentence) > 1:
                divided_space = remaining_space/(len(sentence)-1)
                if divided_space - int(divided_space) == 0:
                    divided_space = int(divided_space)  # no extra space
                elif divided_space - int(divided_space) > 0.5:
                    # 5/3 = 1.666
                    # 2spaces * 2 and 2-1spaces * 1
                    # 8/3 = 2.666
                    # 3spaces * 2 and 3-1spaces * 1
                    divided_space = int(divided_space) + 1  # remove extra space
                    last_space_minus_one = True

                elif divided_space - int(divided_space) <= 0.5:
                    # 8/7 = 1.1 
                    # 1space*6 + 1+1spaces*1
                    # 9/2 = 4.5 
                    # 4spaces * 1 and 4+1spaces * 1
                    divided_space = int(divided_space)  #
                    last_space_plus_one = True
                
            print(remaining_space, divided_space, last_space_minus_one, last_space_plus_one)
            if len(sentence) > 1:
                result_sentence += sentence[0] 
                for j in range(1, len(sentence)):
                    if last_space_plus_one:
                        if j == len(sentence) - 1:
                            result_sentence += int(divided_space) * ' ' 
                        else:
                            result_sentence += int(divided_space+1) * ' ' 
                    elif last_space_minus_one:
                        if j == len(sentence) - 1:
                            result_sentence += int(divided_space-1) * ' ' 
                        else:
                            result_sentence += divided_space * ' ' 
                    else:
                        result_sentence += divided_space * ' ' 
                    result_sentence += sentence[j]
            if len(sentence) == 1:
                result_sentence += sentence[0] 
                result_sentence += int(divided_space-1) * ' '
            # print(result_sentence)
            
            # append resulting sentence
            result.append(result_sentence)
            
            # reset sentence
            result_sentence = ""
        
        # for last sentence, left justified
        sentence, remaining_space = sentences[len(sentences)-1], remaining_spaces[len(sentences)-1]
        count = 0
        for word in sentence:
            result_sentence += word + " "
            count += 1
        result_sentence += int(remaining_space - count) * ' '
        result.append(result_sentence)
        return result