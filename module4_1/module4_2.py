def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    return
#inner_function() - ошибка имя внутренней функции не определено
test_function()
