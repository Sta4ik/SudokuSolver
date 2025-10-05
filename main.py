from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def isValidNum(num, row, col, field):
    for i in range(0, 9):
        if field[row][i] == num:
            return False
        if field[i][col] == num:
            return False

    boxRow = (row // 3) * 3
    boxCol = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if field[boxRow + i][boxCol + j] == num:
                return False
    return True

def findEmpty(field):
    for row in range(0, 9):
        for col in range(0, 9):
            if field[row][col] == '':
                return (row, col)
    return None

def solveSudoku(field):
    empty = findEmpty(field)
    if empty == None:
        return True

    row, col = empty
    for i in range(1, 10):
        num = str(i)
        if isValidNum(num, row, col, field):
            field[row][col] = num
            if solveSudoku(field):
                return True
            field[row][col] = ''
    return False

def main():
    driver = webdriver.Chrome()
    driver.get('https://absite.ru/sudoku')

    field = []
    for rowIndx in range(0, 9):
        row = []
        for colIndx in range(0, 9):
            element = rowIndx * 9 + colIndx
            row.append(driver.find_element(By.XPATH, f'//*[@id="{element}"]').get_attribute('textContent'))
        field.append(row)

    solveSudoku(field)

    driver.find_element(By.XPATH, '//*[@id="0"]').click()
    for row in range(9):
        for col in range(9):
            value = field[row][col]
            driver.switch_to.active_element.send_keys(value)
            driver.switch_to.active_element.send_keys(Keys.ARROW_RIGHT)

if __name__ == "__main__":
    main()