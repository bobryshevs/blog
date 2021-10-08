from structure import jwt_wrapper
import jwt

a = jwt.encode(payload={"exp": 0}, key='123')
jwt.decode(a, key='123', algorithms=['HS256'])