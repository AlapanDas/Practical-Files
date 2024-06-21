def countNode(h):
     if h=='':
          return 0
     else:
          return 1+countNode(h.link)
     
