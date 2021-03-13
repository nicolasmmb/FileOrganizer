import shutil
import time
import os
import platform
def clear(): return os.system('cls')
def pause(): return os.system('pause')


EXTENCOES_DICIONARIO = {
    'IMAGENS':      ['.jpg', '.png', '.gif', '.ico', '.psd', '.webp', '.raw', '.jpeg', '.lif', '.bmp', '.tif', '.svg', '.ai', '.webp'],
    'VIDEOS':       ['.mp4', '.mkv', '.avi', '.3gp', '.webm', '.mpeg', '.wmv', '.mov', '.flv'],
    'AUDIO':        ['.mp3', '.flac', '.m4a', '.wav', '.aac'],
    'OFFICE_EXCEL': ['.xls', '.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm', '.xla', '.xlam'],
    'OFFICE_WORD':  ['.doc', '.docx', '.docm', '.dotx', '.dot', '.dotm', '.rtf'],
    'OFFICE_POWER': ['.pptx', '.pptm', '.ppt', '.potx', '.potm', '.pot', '.thmx', '.ppsx', '.ppsm', '.pps', '.odp'],
    'COMPRESSED':   ['.iso', '.zip', '.rar', '.7z', '.tgz', '.tar', '.bz'],
    'DEVELOPMENT':  ['.py', '.c', '.cpp', '.dart', '.js', '.bat', '.sh','.dart'],
    'PROGRAMAS':    ['.exe', '.msi'],
    'OUTROS':       ['.csv', '.sql', '.ini', '.lnk', '.url', '.txt', '.torrent', '.md'],
    'PDFs':         ['.pdf'],
    'MAC_FILES':     ['.dmg', '.app', '.kext', '.pkg']}


def CRIAR_DIRETORIOS(diretorio, nome_pasta):
    try:
        if nome_pasta == "":
            print('>>>: NÃO É POSSIVEL CRIAR PASTAS SEM NOME <<<')
        else:
            os.makedirs(f'{diretorio}{os.sep}{nome_pasta}')  # exist_ok = true
            print(
                f'>>>: DIRETORIO CRIADO COM SUCESSO       >>> "{nome_pasta}"')

    except(OSError, FileExistsError):
        if os.path.isdir(diretorio):
            print(
                f'>>>: O DIRETORIO JÁ EXISTE:             >>>" {diretorio}{os.sep}{nome_pasta}"')
        else:
            print(
                f'>>>: NÃO FOI POSSIVEL CRIAR O DIRETORIO >>> "{nome_pasta}"')
        pass

    finally:
        # if os.path.isdir(diretorio_atual):
        #    print(f'>>> O DIRETORIO JÁ EXISTE: "{diretorio_atual}\{nome_pasta}"')
        pass


def REMOVER_DIRETORIO_VAZIO(diretorio):
    PASTAS_LISTA = []
    for diretorios in os.listdir(diretorio):
        PASTAS_LISTA.append(diretorios)

    for i in range(0, len(PASTAS_LISTA)):
        try:
            os.rmdir(f'{diretorio}{os.sep}{PASTAS_LISTA[i]}')
        except:
            print(
                f'>>>: A PASTA NÃO ESTA VAZIA, OU NÃO PODE SER MODIFICADA: {diretorio}{os.sep}{PASTAS_LISTA[i]}')
            i+1


def ORGANIZA_PASTA(diretorio, lista_extensoes, nome_pasta):
    for dados in os.listdir(diretorio):
        filename, file_ext = os.path.splitext(dados)
        try:
            if not file_ext:
                pass
            elif file_ext.lower() in lista_extensoes:
                shutil.move(
                    os.path.join(diretorio, f'{filename}{file_ext}'),
                    os.path.join(diretorio, nome_pasta, f'{filename}{file_ext}'))
        finally:
            pass


def PRINT_LAYER():
    print('=-='*40)


def PRINT_INFO():
    PRINT_LAYER()
    print('=  1: OBSERVAÇÕES: NÃO SERA POSSÍVEL REVERTER AS ALTERAÇÕES APOS A EXECUÇÃO DO PROGRAMA\n=')
    print('=  2: OBSERVAÇÕES: USE COM CAUTELA, DE PREFERÊNCIA EM PASTAS QUE VOCE SAIBA QUE NÃO TENHA INFORMACOES IMPORTANTES')
    PRINT_LAYER()
    print('\n')


def MODULES_INSTALL():
    try:
        os.system('pip install shutil')
    except:
        pass


def EXEC_PROGRAMA():
    # MODULES_INSTALL()
    clear()
    PRINT_INFO()

    diretorio_atual = input(
        '>>> COLOQUE O DIRETORIO DA PASTA PARA SER ORGANIZADA: ')
    PRINT_LAYER()

    for i in EXTENCOES_DICIONARIO:
        CRIAR_DIRETORIOS(diretorio_atual, i)
        ORGANIZA_PASTA(diretorio_atual, EXTENCOES_DICIONARIO[i], i)
        # ORGANIZA_PASTA(diretorio_atual,EXTENCOES_DICIONARIO[i],i)

    PRINT_LAYER()
    time.sleep(1)

    REMOVER_DIRETORIO_VAZIO(diretorio_atual)
    PRINT_LAYER()


EXEC_PROGRAMA()
pause()
