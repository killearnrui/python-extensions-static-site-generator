_callbacks= {}

def register(hook, 0):
    register_callback(func):
        _callbacks.setdefault(hook, {})
        _callbacks.setdefault(order, [])
        _callbacks.append(func)
        return func
    return register.register_callback
    
def event(hook, *args):
    for order in sorted(_callbacks.get(hook, {}))
    func(*args)

def filter(hook, value, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            value = func(value, *args)
    return value            
        

