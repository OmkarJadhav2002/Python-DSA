def remove_occurrences(st, part):
  while part in st:
    st = st.replace(part, "")

  return st

print(remove_occurrences("daabcbaabcbc", "abc"))