# JinRongExtractScript
金融出版社文件拆分脚本

运行环境：

    Python2.7

    Python3

    JDK8


数据提取流程：

1.提取所有的PDF源文件，文件名重命名为当前文件夹名，并形成参照文件PDF_File.txt【GetAllPDF.py】

2.提取所有的XML目录信息，文件名重命名为当前文件夹名，并形成参照文件XML_MULU_File.txt【GetAllMuluXML.py】

3.提取所有的XML章节信息，文件夹名重命名为当前文件夹名，并形成参照文件XML_Chapter_File.txt【GetChapterXML.py】


4.根据提取的目录XML信息，提取目录信息（目录名称，开始页码，文件名称，目录层级），并形成参照文件parseMuluXML.txt【GetMuluInfo.py】

5.根据MULU_File.txt计算目录层级，得出下级目录的上级目录名称，并形成参照文件MULU_Level_File.txt【GetLevelName.py】


6.生成校审文件JiaoShenFile.txt,生成一个外键【GetJiaoShenFile.py】

7.生成偏移对照文件Check_Page_Offset_File.txt，生成一个外键【GetPageOffset.py】

8.由数据库根据两个生成校对表格,校对完成后再生成Page_Offset_File.txt

1）先切分，多切一页，再审核。

2）默认生成页码，校对页码后再做切分。


9.获取所有的PDF文件名，对条目、PDF文件生成唯一GUID【GetAllBookName.py,java程序生成】

10.编写脚本根据起始偏移拆分PDF文件【GenFile.py】


11.查找所有的Tag标签【GetAllTag.py】

12.根据碎片化XML文件提取章、节、小节正文内容(去除额外标签)，生成临时文件Check_Content_File.txt【GetContent.py】

13.对提取的信息进行中文空格去除，英文空格保留处理（使用Python3）形成参照文件Content_File.txt。【DealContentFile.py】

14.使用Python3进行入库处理（对文本数据进行转译处理）【CreateInsertContentSQL.py】


15.对数据进行散列存储，？采用多层hash还是bookName散列

16.提取PDF的元数据XML信息，形成参照文件XML_BookINFO_File.txt【GetAllBookXML.py】

17.解析PDF元数据XML信息，提取元信息，形成参照文件BookInfo_File.txt【GetBookInfo.py】

18.校对信息，信息入库


19.通过XML信息提取图片、图表信息（待定，将来只提取图表，看有多少类型：formula，table）,形成参照文件All_Image_Info.txt【All_Image_Info.py】

20.提取所有的图片源文件，形成参照文件ALL_IMAGE_File.txt【GetAllImage.py】

21.校对图片信息，保持数量一致。


22.计算目录偏移，做目录切分

23.提取单本PDF文本数据，形成参照文件Content_PDF_File.txt，使用Python3入库。【同14】
