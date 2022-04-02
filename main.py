from InformationFrame import InformationFrame


def main():
    I = InformationFrame("DataFrame1", "A2Data")
    I.displayFrameMetaData()
    print()
    I.displayCells(['B2'])
    I.displayRow(0)
    I.displayCells(['A1', 'B2', 'E2'])
    print(I.sumCell(['A1', 'B2', 'E2']))
    print(I.avgCell(['A1', 'B2', 'E2']))
    print(I.minCell(['A1', 'B2', 'E2']))
    print(I.maxCell(['A1', 'B2', 'E2']))


if __name__ == "__main__":
    main()
