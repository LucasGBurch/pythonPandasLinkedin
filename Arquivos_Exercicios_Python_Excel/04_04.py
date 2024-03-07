# Geração de Código de Barras
# Biblioteca barcode (Geração do Código de Barras)
# Biblioteca tempfile (Criação de arquivos temporários)

from barcode.writer import ImageWriter
import tempfile
import barcode as bc
import xlwings as xw

wb = xw.Book(r'04_04_BarCode.xlsx')
ws = xw.sheets[0]

rng = ws['A1']
id_produtos = rng.options(expand='down', ndim=1).value

barcode_format = bc.get_barcode_class('ean')  # code39

for ix, id_prod in enumerate(id_produtos):

    my_barcode = barcode_format(
        str(id_prod), writer=ImageWriter())  # , add_checksum=False

    with tempfile.TemporaryDirectory() as td:

        caminho = r'c:\temp\imagem'
        my_barcode.save(caminho)

        rng_destino = rng.offset(row_offset=ix, column_offset=1)
        ws.pictures.add(caminho + '.png',
                        left=10+rng_destino.left,
                        top=1+rng_destino.top,
                        height=60
                        )
