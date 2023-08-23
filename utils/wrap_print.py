import textwrap as tr

def wrap_print(string):
    print(tr.fill(string, width=150, 
                  break_long_words=False, 
                  break_on_hyphens=False, 
                  drop_whitespace=True, 
                  fix_sentence_endings = False, 
                  replace_whitespace= False))