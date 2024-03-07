# Geração de QR Code a partir do VBA
# Biblioteca segno (Geração do QRCode)
# Biblioteca tempfile (Criação de arquivos temporários)

import tempfile
import segno
import xlwings as xw

wb = xw.Book(r'04_03_QRCode.xlsm')
ws = xw.sheets[0]

rng = ws['A1']
site = rng.options(expand='down', ndim=1).value

for ix, url in enumerate(site):

    qr = segno.make(url)

    with tempfile.TemporaryDirectory() as td:

        # Para quem não tem o 365, salvar em png ou jpg
        caminho = f'{td}/qr_code.svg'

        qr.save(caminho, scale=2, border=1, finder_dark='#343536')

        rng_destino = rng.offset(row_offset=ix, column_offset=1)
        ws.pictures.add(caminho,
                        left=rng_destino.left,
                        top=rng_destino.top
                        )
