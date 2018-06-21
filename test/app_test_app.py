try:
    from singlesiding import QSingleApplication
except ModuleNotFoundError:
    print('ModuleNotFoundError ...')
    import os
    import sys
    cwd = os.getcwd()
    print('    cwd: %s' % cwd)
    if cwd not in sys.path:
        sys.path.append(cwd)
    from singlesiding import QSingleApplication


def main():
    app = QSingleApplication()
    app.setOrganizationName("test")
    app.setApplicationName("test app")
    app.setApplicationVersion("1")
    app.ensure_single()
    return app


if __name__ == '__main__':
    app = main()
    app.exec_()
