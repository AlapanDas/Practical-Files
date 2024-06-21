def display(h):
     if h=="":
          return
     else:
          print(h.data)
          display(h.link)
