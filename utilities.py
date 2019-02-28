import hashlib

def gen_key(email, positions):
    print str(positions)
    return hashlib.sha256(email + str(positions)).hexdigest()


def invalid_request():
    res = dict()
    res['message'] = 'invalid request'

    return res
# print gen_key('minikie2@naver.com', '{test:test,test1:test1}2')