from rest_framework.renderers import JSONRenderer


class MyJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # render方法将所有响应的结果（dict）转为json
        # data是方法中return Response(serializer.data)中的数据
        try:
            code = data.pop('code')
        except:
            code = 200
        try:
            msg = data.pop('msg')
        except:
            msg = 'success'
        try:
            result = data.pop('data')
        except:
            result = data
        # 告诉浏览器是正常的访问
        renderer_context['response'].status_code = 200
        res = {'code': code, 'msg': msg, 'data': result}
        # 再去调用父类super().render(res)将字典res转为json格式
        return super().render(res)
