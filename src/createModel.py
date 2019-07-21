def main():
    mod1 = model()
    mod1.model_name = "XML Veracity Model"
    d1 = dimension("XML 文件宣告")
    d2 = dimension("XML 文件結構")

    mod1.set_dimensions(d1)
    mod1.set_dimensions(d2)

    d1.set_attributes(document_version())
    d1.set_attributes(document_encode())
    d1.set_attributes(document_standalone())

    d2.set_attributes(document_vaild())
    d2.set_attributes(document_depth())
