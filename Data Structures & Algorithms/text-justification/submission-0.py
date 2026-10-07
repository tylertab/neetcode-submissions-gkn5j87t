class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        outputchars = []
        i = 0
        curr = []
        currchars = 0
        while i < len(words):
            if  len(curr) + currchars + len(words[i]) <= maxWidth:
                currchars += len(words[i])
                curr.append(words[i])
                
            else:
                output.append(curr.copy())
                outputchars.append(currchars)
                curr = [words[i]]
                currchars = len(words[i])
            i += 1

        
        for i in range(len(output)):
            words, charcount = output[i], outputchars[i]
            amtspaces = len(words) - 1
            extraspaces = maxWidth - (charcount + amtspaces)
            if amtspaces == 0:
                endspace = " " * (maxWidth - len(words[0]))
                output[i] = words[0] + endspace
            elif extraspaces == 0:
                output[i] = " ".join(words)
            elif extraspaces % amtspaces == 0:
                space = " " * ((extraspaces // amtspaces) + 1)
                output[i] = space.join(words)
            else:
                minspace = " " * ((extraspaces // amtspaces) + 1)
                needextra = extraspaces % amtspaces
                currr = words[0]
                for j in range(1, len(words)):
                    if needextra != 0:
                        needextra -= 1
                        currr += minspace + " " + words[j]
                    else:
                        currr += minspace + words[j]
                output[i] = currr

        if curr != []:
            output.append(" ".join(curr.copy()))
            endspace = " " * (maxWidth - len(output[-1]))
            output[-1] += endspace
        
            

        print(output)
        return output