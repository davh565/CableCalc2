import xlwings as xw


@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2 * (x + y)


@xw.func
def add_one(data):
    return [[cell + 1 for cell in row] for row in data]


@xw.func
@xw.arg('xl_app', vba='Application')
def get_caller_address(xl_app):
    return xl_app.Caller.Address
