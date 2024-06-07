class Table:
    def __init__(self,length):
        self.table = {}
        self.tableLength = 0

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.dataBase = {name:Table(column) for name,column in zip(names,columns)}

    def insertRow(self, name: str, row: List[str]) -> None:
        table_ = self.dataBase[name]
        table_.tableLength += 1
        table_.table[table_.tableLength] = row


    def deleteRow(self, name: str, rowId: int) -> None:
        self.dataBase[name].table.pop(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.dataBase[name].table[rowId][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)