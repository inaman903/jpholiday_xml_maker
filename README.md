# jpholiday_xml_maker
指定期間内の日本の祝日の一覧をXMLで出力します

## install
pip install jpholiday

## usage
python jpholiday_xml_maker 2010/1/1 2019/1/1

## xml
```xml
<holidays start="開始日" end="終了日">
    <holiday date="日付" name="名前"/>
<holidays/>
```
