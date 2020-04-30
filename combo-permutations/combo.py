def combos(word):
  # calls method permutations for string word
  combos = permutations(str(word))

  # do the regression of combos for each one permutation letter
  regression_combos = []
  for count in range(1, len(word)):
    for p in combos:
      if(p[:-count] not in regression_combos):
        regression_combos.append(p[:-count])

  # concatenate combos with regressionated combos
  combos += regression_combos

  # sort combos by length of values
  combos.sort(key=len)

  # print each one combo
  print("------- PERMUTATIONS --------")
  print("TOTAL: {} combos".format(len(combos)), end='\n\n')

  for combo in combos:
    print(''.join(combo))

def permutations(word):
  word_list = list(word)
  length_list = len(word_list)

  # return word list in array if length is 1
  if length_list == 1:
    return [word_list]

  permutated_word = []

  for index in range(length_list):
    letter = word_list[index]

    # remove index letter from list
    list_without_index = list(word_list)
    list_without_index.remove(letter)

    # do the permutation with new list
    for permutated in permutations(list_without_index):
      # append permutated with the word of index
      permutated_word.append([letter] + permutated)
  return permutated_word

combos('ABC')
