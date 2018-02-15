from ultron.objects import Admin, Client

def testfunc(clientname, adminname, reportname,
             teststr, testlst, testdct={},
             testint=0, testbool=False):
    """
    Just a demo task
    """
    client = Client(clientname, adminname, reportname)
    admin = Admin(adminname)
    client.state.update({
        'test': 'SUCCESS',
        'admin': admin.name,
        'passedstr': teststr,
        'passedlst': testlst,
        'passeddct': testdct,
        'passedint': testint,
        'passedbool': testbool
    })
    client.save()
    return {'conclusion': 'Test is successful'}
