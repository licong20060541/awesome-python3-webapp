import test_orm 
import asyncio
from test_models import User, Blog, Comment

async def test(loop):
    await test_orm.create_pool(loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()