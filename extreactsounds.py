import re


def extractSoudsSections(section):
  soundLinesPattern = re.compile(r'\*\s\{{2}.+\}{2}')
  lineMatches = soundLinesPattern.finditer(section)

  finalSounds = ""
  for lineMatch in lineMatches:
    line = string[lineMatch.start():lineMatch.end()]
    pattern = re.compile(r"\{{2}(\ba\|[\w\s]+\b|\bIPA.+|\benPR.+\b|\brhymes.+)\}{2}")

    matches = pattern.finditer(line)

    finalLine = ""
    for match in matches:
      start = match.start()
      end = match.end()
      finalLine+= line[start+2:end-2]+","
    finalSounds+="* "+finalLine+"\n"
  return finalSounds


string = '''
   * {{a|US}}, {{a|UK}} {{enPR|fŭk}}, {{IPA2|/fʌk/}}
* {{rhymes|ʌk}}
* 
* {{a|some Northern English accents}} {{enPR|fo͝ok}}, {{IPA2|/fʊk/}}
* {{rhymes|ʊk}}
'''

print(extractSoudsSections(string))
