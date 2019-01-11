try:
    import singlesiding
except ModuleNotFoundError:
    print('ModuleNotFoundError ...')
    import os
    import sys
    cwd = os.getcwd()
    print('    cwd: %s' % cwd)
    if cwd not in sys.path:
        sys.path.append(cwd)
    import singlesiding


def main():
    app = singlesiding.initialize('test', 'test app', '1', 'message!')
    return app


def _on_msg_receive(msg):
    print('msg: %s' % msg)


if __name__ == '__main__':
    app = main()
    app.message_received.connect(_on_msg_receive)
    app.exec_()
