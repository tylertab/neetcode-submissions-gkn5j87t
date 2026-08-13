class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        
        for email in emails:
            processed = ""
            hasat = -1
            domaindot = 0
            i = 0
            while i < len(email):
                if email[i] == '@':
                    hasat = i
                    processed += email[i]
                
                elif hasat == -1:
                    if email[i] == '+':
                        while i < len(email) - 1 and email[i + 1] != "@":
                            i += 1
                    elif email[i] != '.':
                        processed += email[i]

                else:
                    processed += email[i]
                i += 1
            s.add(processed)
        print(s)
        return len(s)
                    

                
    
