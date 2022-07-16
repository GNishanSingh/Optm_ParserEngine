import re, json,os
import argparse

def ParseData (Data, RegexArray):
    result = {}
    for Regex in RegexArray['All']:
        search = re.search(Regex,Data)
        if search:
            result.update(search.groupdict())
    if RegexArray['Conditional']:
        try:
            Regexes = RegexArray['Conditional']['Conditions'][result[RegexArray['Conditional']['ConditionField']]]
            for regex in Regexes:
                search = re.search(RegexArray['Conditional']['Regexes'][regex],result[RegexArray['Conditional']['ParseField']])
                if search:
                    result.update(search.groupdict())
        except:
            None
    return json.dumps(result,indent=4)
def Optm_ParserEngine(Parsername,Data):
    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Config.json'))
    Config = json.load(f)
    f.close()
    return ParseData(Data,Config['regex'][Parsername])
def ShowParser():
    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Config.json'))
    Config = json.load(f)
    f.close()
    return Config['Parser']
if __name__ == '__main__':
    Description = '''
# Optimized Parser Engine

    '''
    arguments = argparse.ArgumentParser(description=Description)
    arguments.add_argument('--show',action=argparse.BooleanOptionalAction,dest='Show',help='Provide configuration file path',required=False)
    arguments.add_argument('-p','--parsername',dest='parser',help='Provide the parser groupname contains your regex',required=False)
    arguments.add_argument('-d',dest='data',help='Provide the data which you want to parse',required=False)

    args = arguments.parse_args()
    if args.parser:
        print(Optm_ParserEngine(args.parser,args.data))
    elif args.Show:
        print('\n'.join(ShowParser()))