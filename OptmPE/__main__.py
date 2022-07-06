import re, json
import argparse

def ParseData (Data, RegexArray):
    result = {}
    for Regex in RegexArray['All']:
        search = re.search(Regex,Data)
        if search:
            result.update(search.groupdict())
    if RegexArray['Conditional']:
        try:
            for Regex in RegexArray['Conditional']['Regex'][result[RegexArray['Conditional']['ConditionField']]]:
                search = re.search(Regex,result[RegexArray['Conditional']['ParseField']])
                if search:
                    result.update(search.groupdict())
        except:
            None
    return json.dumps(result,indent=4)
def Optm_ParserEngine(configpath,Parsername,Data):
    f = open(configpath)
    Config = json.load(f)
    f.close()
    return ParseData(Data,Config['regex'][Parsername])
if __name__ == '__main__':
    Description = '''
# Optimized Parser Engine

    '''
    arguments = argparse.ArgumentParser(description=Description)
    arguments.add_argument('--configpath',dest='configpath',help='Provide configuration file path',required=True)
    arguments.add_argument('--parsername',dest='parser',help='Provide the parser groupname contains your regex',required=True)
    arguments.add_argument('--d',dest='data',help='Provide the data which you want to parse',required=True)
    args = arguments.parse_args()
    print(Optm_ParserEngine(args.configpath,args.parser,args.data))