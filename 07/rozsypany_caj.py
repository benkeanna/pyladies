hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔ"
hira_count = 0

katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ"
kata_count = 0

with open("rozsypany_caj.txt", encoding ='utf-8') as my_file:
    for line in my_file:
        for ch in line:
            if ch in hiragana:
                hira_count = hira_count + 1
            elif ch in katakana:
                kata_count = kata_count + 1
            else:
                pass

    print("Počet znaků z abecedy hiragana je ", hira_count,
          ", počet znaků z abecedy katakana je ", kata_count, ".")
