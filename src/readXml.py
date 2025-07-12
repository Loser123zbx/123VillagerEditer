import xml.parsers.expat as expat 
import requests
import xmltodict

class Block():  
    Bid = ''
    Bname = ''
    BtextID = ''
    def __init__(self, id, name, tid):
        self.Bid = id
        self.Bname = name
        self.BtextID = tid

def getIDs(url = 'https://minecraft-ids.grahamedgecombe.com/'):
    response = requests.get(url)
    xmlData = response.text
    f = open(file= 'blocks.xml',mode= 'w', encoding="utf-8")
    xmlData = '<table id="rows" class="items">' + xmlData.split('<table id="rows" class="items">')[1]
    xmlData = xmlData.split('</table>')[0] + "</table>"
    f.write(xmlData)
    f.close()


def getBlocksData(filePath = 'blocks.xml'):
    try:  
        parser = expat.ParserCreate()  
        with open(filePath, 'r', encoding='utf-8') as file:  # 确保文件以正确的编码打开  
            xmlData = file.read()

            if not xmlData:  # 检查文件是否为空  
                print("XML文件为空，无法解析。")  
                return  
            parser.Parse(xmlData, True)  
        print("XML文件解析成功！")  
        return xmlData
    except FileNotFoundError:  
        print(f"文件 {filePath} 未找到。")  
    except expat.ExpatError as e:  
        print(f"解析XML时出错: {e}")  


        

if __name__ == "__main__":
    getIDs()
    a = (getBlocksData())
    f = open("test.txt",'w')
    f.write(str(a))
    f.close()
 