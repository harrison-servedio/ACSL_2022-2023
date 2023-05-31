def findARow(original, unused, rows):
    og_string = original
    # og_string = "KWIC is an acryonym for Key Word in Context, the most common format for concordance lines which is used for indexing in context."

    og_string = og_string.replace(",", " ,")
    og_string = og_string.replace(".", " .")
    og_string = og_string.replace("?", " ?")
    og_string = og_string.replace(";", " ;")
    og_string = og_string.replace("!", " !")
    og_string = og_string.replace(":", " :")
    og_strings = og_string.split(" ")
    # print(og_strings)

    # unimportants = "for in the"
    unimportants = unused

    unimportants_list = unimportants.split(" ")

    words_to_parse = [string for string in og_strings if string.lower() not in unimportants_list and string not in [",",".","?",";","!",":"]]
    words_to_parse = [*set(words_to_parse)]
    sorted_words_to_parse = sorted(words_to_parse, key=str.casefold)

    numbers = rows
    # numbers = "7 15"
    numbers = numbers.split(" ")

    # print(sorted_words_to_parse)

    def find_indices(l, word):
        g = []
        for i in range(len(l)):
            if l[i] == word:
                g.append(i)
        return g

    table = []
    max_before = 0
    max_word = 0
    max_after = 0

    for word in sorted_words_to_parse:

        indices = find_indices(og_strings, word)
        

        for index in indices:

            backwards = []
            for i in range(1,4):
                if index-i < 0:
                    break
                elif og_strings[index-i].lower() in unimportants_list:
                    break
                elif og_strings[index-i] in [",",".","?",";","!",":"]:
                    break
                backwards.insert(0, og_strings[index-i])
            
            forwards = []
            for i in range(1,4):
                if index+i > len(og_strings):
                    break
                elif og_strings[index+i].lower() in unimportants_list:
                    break
                elif og_strings[index+i] in [",",".","?",";","!",":"]:
                    break
                forwards.append(og_strings[index+i])

            if len(word) >  max_word:
                max_word = len(word)
            if len(" ".join(backwards)) > max_before:
                max_before = len(" ".join(backwards))
            if len(" ".join(forwards)) > max_after:
                max_after = len(" ".join(forwards))

            total = []
            total.append(" ".join(backwards))
            total.append(word)
            total.append(" ".join(forwards))

            table.append(total)

    for row in table:
        for i in range(3):
            if i == 0:
                to_add = max_before - len(row[i])
                row[i] = row[i] + "-"*to_add
            elif i == 1:
                to_add = max_word - len(row[i])
                row[i] = "<" + row[i] + "-"*to_add + ">"
            elif i == 2:
                to_add = max_after - len(row[i])
                row[i] = row[i] + "-"*to_add

    counts = []
    for i in range(int(numbers[0])-1, int(numbers[1])):
        count = " ".join(table[i]).count("-")
        counts.append(count)

    toprintidx = find_indices(counts, min(counts))[0] + int(numbers[0]) -1
    final = " ".join(table[toprintidx])

    return final

print(findARow("KWIC is an acronym for Key Word In Context, the most common format for concordance lines which is used for indexing in context.", "for in the", "7 15"))