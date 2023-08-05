import re


def main():
    print(convert(input("Hours: ")))



def convert(s):
    if matches := re.search(r"^(\d+)(?::)?(\d+)? AM to (\d+)(?::)?(\d+)? PM$", s):   
        if 0 < int(matches.group(1)) <= 12:
            hour_am = int(matches.group(1))
        else:
            raise ValueError("Time not correct.")
        
        if matches.group(2) is None:
            min_am = 0
        elif 0 <= int(matches.group(2)) < 60:
            min_am = int(matches.group(2))
        else:
            raise ValueError("Time not correct")
        
        if 0 < int(matches.group(3)) <= 12:
            hour_pm = int(matches.group(3)) + 12
            if hour_pm == 24:
                hour_pm = 12    
        else:
            raise ValueError("Time not correct.")
        
        if matches.group(4) is None:
            min_pm = 0
        elif 0 <= int(matches.group(4)) < 60:
            min_pm = int(matches.group(4))
        else:
            raise ValueError("Time not correct")
        
        return f"{hour_am:02}:{min_am:02} to {hour_pm:02}:{min_pm:02}"
    else:
        raise ValueError("Not correct format.")
    
if __name__ == "__main__":
    main()