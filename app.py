start_dict = {
  "d": 2,
  "a": {
    "b": {
      "c": 1,
      "c2": 2
    }
  },
  "x":{
    "y":5,
    "t":3
  }
}


end = { "a.b.c": 1, "d": 2 }

def find(obj, keys_found = []):
    breakpoint()
    for k,v in obj.items():
        if type(v) is dict:
            keys_found.append(k)
            find(v, keys_found)
            keys_found = []
        if type(v) is int:
            joint_path = ".".join([*keys_found, k])
            end_struct[joint_path] = v
            

        

if __name__ == "__main__":
    end_struct = {}
    find(start_dict)
    print(end_struct)
        





