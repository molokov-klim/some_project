##################################################################################################################################
# ; ВНИМАНИЕ! При добавлении новых тегов убедитесь в работоспособности утилиты. Если всё хорошо, закоммитьте!
# ; Для создания или правки тега сделайте запись по образцу:
# ; [XXXX]            // номер тега
# ; Type =  XXXX      // тип тега
# ; Head =            // не используется (пока)
# ; Name =  XXXX      // введите название тега
# ;
# ; Используйте следующие типы:
# ; BYTE	     - целое число 1 байт
# ; INT16        - целое число 2 байта
# ; INT32        - целое число 4 байта
# ; VLN          - байты представляют собой число, LE
# ; FPD          - фискальный признак, последние 4 байта с конца
# ; STRING       - байты представляют собой символы
# ; COINS        - цена в копейках, при выводе число делится на 100 (в рубли), байты представляют собой число, LE
# ; UNIXTIME     - дата и время в формате UnixTime
# ; FVLN         - дробное число, первый байт - позиция запятой, остальные байты представляют собой число, LE, применяется для количества
# ; STLV         - тег представляет собой структуру STLV
# ; ENUM или SET - множество значений в зависимости от числа, байты представляют собой число, LE
# ;      Для использования ENUM или SET необходимо также задать значения (см. пример тег 1209):
# ;      [XXXX]
# ;      Type =  ENUM
# ;      Head =
# ;      Name =  XXXX
# ;      Value1 = Значение 1 (соотв. числу 1)
# ;      Value2 = Значение 2 (соотв. числу 2)
# ;      Value7 = Значение 7 (соотв. числу 7)
# ; и.т.п
# ; BITS        - значением является множество, задаваемое битовой маской
# ;      Для использования BITS необходимо также задать значения (см. пример тег 1057):
# ;      [XXXX]
# ;      Type =  ENUM
# ;      Head =
# ;      Name =  XXXX
# ;      BIT0 = Значение 1 (соотв. бит 0 = 1)
# ;      BIT1 = Значение 2 (соотв. бит 1 = 1)
# ;      BIT2 = Значение 3 (соотв. бит 2 = 1)
# BYTES - массив байт
##################################################################################################################################

BYTE = 'BYTE'
INT16 = 'INT16'
INT32 = 'INT32'
VLN = 'VLN'
FPD = 'FPD'
STRING = 'STRING'
COINS = 'COINS'
UNIXTIME = 'UNIXTIME'
FVLN = 'FVLN'
STLV = 'STLV'
ENUM = 'ENUM'
SET = 'SET'
BITS = 'BITS'
BYTES = 'BYTES'

tags = {
    "6": {
        "Type": STLV,
        "Head": "ОТЧЁТ О ЗАКРЫТИИ ФИСКАЛЬНОГО НАКОПИТЕЛЯ",
        "Name": "отчёт о закрытии фискального накопителя",
    },
    "106": {
        "Type": STLV,
        "Head": "ОТЧЁТ О ЗАКРЫТИИ ФИСКАЛЬНОГО НАКОПИТЕЛЯ",
        "Name": "отчёт о закрытии фискального накопителя",
    },
    "7": {
        "Type": STLV,
        "Head": "ПОДТВЕРЖДЕНИЕ ОПЕРАТОРА",
        "Name": "подтверждение оператора",
    },
    "107": {
        "Type": STLV,
        "Head": "ПОДТВЕРЖДЕНИЕ ОПЕРАТОРА",
        "Name": "подтверждение оператора",
    },
    "1001": {
        "Type": BYTE,
        "Head": "АВТОМАТ.РЕЖИМ:",
        "Name": "автоматический режим",
    },
    "1002": {
        "Type": BYTE,
        "Head": "АВТОНОМН.РЕЖИМ:",
        "Name": "автономный режим",
    },
    "1003": {
        "Type": "",
        "Head": "адрес банковского агента для банковских агентов",
        "Name": "",
    },
    "1004": {
        "Type": "",
        "Head": "адрес для банковского субагента для банковских агентов",
        "Name": "",
    },
    "1005": {
        "Type": STRING,
        "Head": "АДР.ОП.ПЕРЕВОДА:",
        "Name": "адрес оператора по переводу денежных средств для банковских агентов",
    },
    "1006": {
        "Type": "",
        "Head": "адрес платежного агента для платежных агентов",
        "Name": "",
    },
    "1007": {
        "Type": "",
        "Head": "адрес платежного субагента для платежных агентов",
        "Name": "",
    },
    "1008": {
        "Type": STRING,
        "Head": "",
        "Name": "адрес покупателя",
    },
    "1009": {
        "Type": STRING,
        "Head": "",
        "Name": "адрес (место) расчетов",
    },
    "1010": {
        "Type": VLN,
        "Head": "ВОЗН.ПЛ.АГЕНТА:",
        "Name": "размер вознаграждения банковского агента (субагента) для банковских агентов",
    },
    "1011": {
        "Type": "",
        "Head": "",
        "Name": "размер вознаграждения платежного агента (субагента) для платежных агентов",
    },
    "1012": {
        "Type": UNIXTIME,
        "Head": "",
        "Name": "дата, время",
    },
    "1013": {
        "Type": STRING,
        "Head": "ЗН ККТ:",
        "Name": "заводской номер ККТ",
    },
    "1014": {
        "Type": "",
        "Head": "",
        "Name": "значение типа строка",
    },
    "1015": {
        "Type": "",
        "Head": "",
        "Name": "значение типа целое",
    },
    "1016": {
        "Type": STRING,
        "Head": "ИНН.ОП.ПЕРЕВОДА:",
        "Name": "ИНН оператора по переводу денежных средств для банковских агентов",
    },
    "1017": {
        "Type": STRING,
        "Head": "ИНН ОФД:",
        "Name": "ИНН ОФД",
    },
    "1018": {
        "Type": STRING,
        "Head": "ИНН:",
        "Name": "ИНН пользователя",
    },
    "1019": {
        "Type": "",
        "Head": "",
        "Name": "информационное сообщение",
    },
    "1020": {
        "Type": COINS,
        "Head": "ИТОГ:",
        "Name": "ИТОГ",
    },
    "1021": {
        "Type": STRING,
        "Head": "КАССИР:",
        "Name": "кассир",
    },
    "1022": {
        "Type": BYTE,
        "Head": "",
        "Name": "код ответа ОФД",
        "Value0": "успешно",
        "Value11": "неисправимая ошибка, содержание документа не распознано",
        "Value14": "ошибка ФЛК при обработке документа",
    },
    "1023": {
        "Type": FVLN,
        "Head": "",
        "Name": "количество",
    },
    "1024": {
        "Type": "",
        "Head": "",
        "Name": "наименование банковского агента для банковских агентов",
    },
    "1025": {
        "Type": "",
        "Head": "",
        "Name": "наименование банковского субагента для банковских агентов",
    },
    "1026": {
        "Type": STRING,
        "Head": "ОПЕРАТОР ПЕРЕВОДА:",
        "Name": "наименование оператора по переводу денежных средств для банковских агентов",
    },
    "1027": {
        "Type": "",
        "Head": "",
        "Name": "наименование платежного агента для платежных агентов",
    },
    "1028": {
        "Type": "",
        "Head": "",
        "Name": "наименование платежного субагента для платежных агентов",
    },
    "1029": {
        "Type": "",
        "Head": "",
        "Name": "наименование реквизита",
    },
    "1030": {
        "Type": STRING,
        "Head": "",
        "Name": "наименование товара",
    },
    "1031": {
        "Type": COINS,
        "Head": "НАЛИЧНЫМИ:",
        "Name": "форма расчета – наличными"
    },
    "1032": {
        "Type": "",
        "Head": "",
        "Name": "налог"
    },
    "1033": {
        "Type": "",
        "Head": "",
        "Name": "налоги"
    },
    "1034": {
        "Type": "",
        "Head": "",
        "Name": "наценка (ставка)"
    },
    "1035": {
        "Type": "",
        "Head": "",
        "Name": "наценка (сумма)"
    },
    "1036": {
        "Type": STRING,
        "Head": "АВТОМАТ:",
        "Name": "номер автомата"
    },
    "1037": {
        "Type": STRING,
        "Head": "РНККТ:",
        "Name": "регистрационный номер ККТ"
    },
    "1038": {
        "Type": INT32,
        "Head": "СМЕНА:",
        "Name": "номер смены"
    },
    "1039": {
        "Type": "",
        "Head": "",
        "Name": "зарезервирован"
    },
    "1040": {
        "Type": INT32,
        "Head": "ФД:",
        "Name": "порядковый номер фискального документа"
    },
    "1041": {
        "Type": STRING,
        "Head": "ФН:",
        "Name": "заводской номер фискального накопителя"
    },
    "1042": {
        "Type": INT32,
        "Head": "",
        "Name": "номер чека за смену"
    },
    "1043": {
        "Type": COINS,
        "Head": "",
        "Name": "общая стоимость позиции с учетом скидок и наценок"
    },
    "1044": {
        "Type": STRING,
        "Head": "ОП.БАНК.АГЕНТА:",
        "Name": "операция банковского агента для банковских агентов"
    },
    "1045": {
        "Type": "",
        "Head": "",
        "Name": "операция банковского субагента для банковских агентов"
    },

    "1046": {
        "Type": STRING,
        "Head": "ОФД:",
        "Name": "ОФД"
    },
    "1047": {
        "Type": "",
        "Head": "",
        "Name": "параметр настройки"
    },
    "1048": {
        "Type": STRING,
        "Head": "",
        "Name": "наименование пользователя"
    },
    "1049": {
        "Type": "",
        "Head": "",
        "Name": "почтовый индекс"
    },
    "1050": {
        "Type": BYTE,
        "Head": "РЕСУРС ФН ИСЧЕРПАН",
        "Name": "признак исчерпания ресурса ФН"
    },
    "1051": {
        "Type": BYTE,
        "Head": "ЗАМЕНИТЬ ФН",
        "Name": "признак необходимости срочной замены ФН"
    },
    "1052": {
        "Type": BYTE,
        "Head": "ФН ПЕРЕПОЛНЕН",
        "Name": "признак переполнения памяти ФН"
    },
    "1053": {
        "Type": BYTE,
        "Head": "ОФД НЕ ОТВЕЧАЕТ",
        "Name": "признак превышения времени ожидания ответа ОФД"
    },
    "1054": {
        "Type": ENUM,
        "Head": "",
        "Name": "признак расчета",
        "Value1": "приход",
        "Value2": "возврат прихода",
        "Value3": "расход",
        "Value4": "возврат расхода"
    },
    "1055": {
        "Type": BITS,
        "Head": "СНО:",
        "Name": "применяемая система налогообложения для чека",
        "BIT0": "общая",
        "BIT1": "упрощенная доход",
        "BIT2": "упрощенная доход минус расход",
        "BIT3": "единый налог на вмененный доход",
        "BIT4": "единый сельскохозяйственный налог",
        "BIT5": "патентная система налогообложения",
        "BIT6": "упрощенная без представления налоговой декларации"
    },
    "1056": {
        "Type": BYTE,
        "Head": "ШФД",
        "Name": "признак шифрования"
    },
    "1057": {
        "Type": BITS,
        "Head": "",
        "Name": "применение платежными агентами (субагентами)",
        "BIT0": "банк. пл. агент",
        "BIT1": "банк. пл. субагент",
        "BIT2": "плат. агент",
        "BIT3": "плат. субагент",
        "BIT4": "поверенный",
        "BIT5": "комиссионер",
        "BIT6": "агент"
    },
    "1058": {
        "Type": "",
        "Head": "",
        "Name": "применение банковскими агентами (субагентами)"
    },
    "1059": {
        "Type": STLV,
        "Head": "",
        "Name": "наименование товара (реквизиты)"
    },
    "1060": {
        "Type": STRING,
        "Head": "САЙТ ФНС:",
        "Name": "сайт налогового органа"
    },
    "1061": {
        "Type": STRING,
        "Head": "",
        "Name": "сайт ОФД"
    },
    "1062": {
        "Type": BITS,
        "Head": "СНО:",
        "Name": "системы налогообложения для регистрации ",
        "BIT0": "ОСН",
        "BIT1": "УСН доход",
        "BIT2": "УСН доход - расход",
        "BIT3": "ЕНВД",
        "BIT4": "ЕСН",
        "BIT5": "Патент"
    },
    "1063": {
        "Type": "",
        "Head": "",
        "Name": "скидка (ставка)"
    },
    "1064": {
        "Type": "",
        "Head": "",
        "Name": "скидка (сумма)"
    },
    "1065": {
        "Type": "",
        "Head": "",
        "Name": "сокращенное наименование налога"
    },
    "1066": {
        "Type": "",
        "Head": "",
        "Name": "сообщение"
    },
    "1067": {
        "Type": "",
        "Head": "",
        "Name": "сообщение оператора для ККТ"
    },
    "1068": {
        "Type": STLV,
        "Head": "",
        "Name": "сообщение оператора для ФН"
    },
    "1069": {
        "Type": "",
        "Head": "",
        "Name": "сообщение оператору"
    },
    "1070": {
        "Type": "",
        "Head": "",
        "Name": "ставка налога"
    },
    "1071": {
        "Type": "",
        "Head": "",
        "Name": "сторно товара (реквизиты)",
        "Note": "запрещается применение реквизита «сторно» в кассовых чеках (БСО), "
                "где отсутствует хотя бы один реквизит «наименование товара»"
    },
    "1072": {
        "Type": "",
        "Head": "",
        "Name": "сумма налога"
    },
    "1073": {
        "Type": STRING,
        "Head": "ТЛФ.ПЛ.АГЕНТА:",
        "Name": "телефон банковского агента для банковских агентов"
    },
    "1074": {
        "Type": STRING,
        "Head": "ТЛФ.ОП.ПР.ПЛАТЕЖА:",
        "Name": "телефон платежного агента для платежных агентов"
    },
    "1075": {
        "Type": STRING,
        "Head": "ТЛФ.ОП.ПЕРЕВОДА:",
        "Name": "телефон оператора по переводу денежных средств для банковских агентов"
    },
    "1076": {
        "Type": "",
        "Head": "",
        "Name": "тип сообщения"
    },
    "1077": {
        "Type": FPD,
        "Head": "ФП:",
        "Name": "фискальный признак документа"
    },
    "1078": {
        "Type": BYTES,
        "Head": "",
        "Name": "фискальный признак оператора"
    },
    "1079": {
        "Type": COINS,
        "Head": "",
        "Name": "цена за единицу"
    },
    "1080": {
        "Type": "",
        "Head": "",
        "Name": "штриховой код"
    },
    "1081": {
        "Type": COINS,
        "Head": "ЭЛЕКТРОННЫМИ:",
        "Name": "форма расчета – электронными"
    },
    "1082": {
        "Type": "",
        "Head": "",
        "Name": "телефон банковского субагента"
    },
    "1083": {
        "Type": "",
        "Head": "",
        "Name": "телефон платежного субагента для банковских агентов"
    },
    "1084": {
        "Type": STLV,
        "Head": "",
        "Name": "дополнительный реквизит пользователя"
    },
    "1085": {
        "Type": STRING,
        "Head": "",
        "Name": "наименование дополнительного реквизита"
    },
    "1086": {
        "Type": STRING,
        "Head": "",
        "Name": "значение дополнительного реквизита"
    },
    "1088": {
        "Type": "",
        "Head": "",
        "Name": "приход наличными"
    },
    "1089": {
        "Type": "",
        "Head": "",
        "Name": "приход электронными"
    },
    "1090": {
        "Type": "",
        "Head": "",
        "Name": "возврат прихода наличными"
    },
    "1091": {
        "Type": "",
        "Head": "",
        "Name": "возврат прихода электронными"
    },
    "1092": {
        "Type": "",
        "Head": "",
        "Name": "расход наличными"
    },
    "1093": {
        "Type": "",
        "Head": "",
        "Name": "расход электронными"
    },
    "1094": {
        "Type": "",
        "Head": "",
        "Name": "возврат расхода наличными"
    },
    "1095": {
        "Type": "",
        "Head": "",
        "Name": "возврат расхода электронными"
    },
    "1096": {
        "Type": "",
        "Head": "",
        "Name": "номер корректируемого фискального документа"
    },
    "1097": {
        "Type": INT32,
        "Head": "НЕПЕРЕДАННЫХ ФД:",
        "Name": "количество непереданных ФД"
    },
    "1098": {
        "Type": UNIXTIME,
        "Head": "ФД НЕ ПЕРЕДАНЫ С:",
        "Name": "дата и время первого из непереданных ФД"
    },
    "1100": {
        "Type": "",
        "Head": "",
        "Name": "номер предписания"
    },
    "1101": {
        "Type": ENUM,
        "Head": "ИЗМ.СВЕД.О ККТ:",
        "Name": "код причины перерегистрации",
        "Value1": "Замена ФН",
        "Value2": "Замена ОФД",
        "Value3": "Изменение реквизитов",
        "Value4": "Изменение настроек ККТ"
    },
    "1102": {
        "Type": COINS,
        "Head": "СУММА НДС 20%",
        "Name": "НДС со ставкой 20%"
    },
    "1103": {
        "Type": COINS,
        "Head": "СУММА НДС 10%",
        "Name": "НДС со ставкой 10%"
    },
    "1104": {
        "Type": COINS,
        "Head": "СУММА НДС 0%",
        "Name": "НДС со ставкой 0% (сумма оборота по налогу)"
    },
    "1105": {
        "Type": COINS,
        "Head": "СУММА БЕЗ НДС:",
        "Name": "НДС не облагается (сумма оборота по налогу)"
    },
    "1106": {
        "Type": COINS,
        "Head": "СУММА НДС 20/120",
        "Name": "НДС с рассчитанной ставкой 20%"
    },
    "1107": {
        "Type": COINS,
        "Head": "СУММА НДС 10/110",
        "Name": "НДС с рассчитанной ставкой 10%"
    },
    "1108": {
        "Type": BYTE,
        "Head": "РАСЧЕТ ТОЛЬКО В ИНТЕРНЕТ",
        "Name": "признак расчетов в сети Интернет"
    },
    "1109": {
        "Type": BYTE,
        "Head": "ТОЛЬКО УСЛУГИ",
        "Name": "признак работы в сфере услуг"
    },
    "1110": {
        "Type": BYTE,
        "Head": "АС БСО",
        "Name": "применяется для формирования БСО"
    },
    "1111": {
        "Type": INT32,
        "Head": "ФД ЗА СМЕНУ",
        "Name": "количество фискальных документов за смену"
    },
    "1112": {
        "Type": STRING,
        "Head": "",
        "Name": "скидка/наценка"
    },
    "1113": {
        "Type": STRING,
        "Head": "",
        "Name": "наименование скидки"
    },
    "1114": {
        "Type": STRING,
        "Head": "",
        "Name": "наименование наценки"
    },
    "1115": {
        "Type": STRING,
        "Head": "",
        "Name": "адрес сайта для проверки ФП"
    },
    "1116": {
        "Type": INT32,
        "Head": "ПЕРВЫЙ НЕПЕРЕДАННЫЙ ФД:",
        "Name": "номер первого непереданного документа"
    },
    "1117": {
        "Type": STRING,
        "Head": "",
        "Name": "адрес отправителя"
    },
    "1118": {
        "Type": INT32,
        "Head": "ЧЕКОВ ЗА СМЕНУ:",
        "Name": "количество кассовых чеков за смену"
    },
    "1119": {
        "Type": "",
        "Head": "",
        "Name": "телефон оператора по приему платежей"
    },
    "1120": {
        "Type": "",
        "Head": "",
        "Name": "код справочника"
    },
    "1121": {
        "Type": "",
        "Head": "",
        "Name": "код классификации товара"
    },
    "1122": {
        "Type": "",
        "Head": "",
        "Name": "сведения о классификации товара"
    },
    "1123": {
        "Type": "",
        "Head": "",
        "Name": "код идентификации товара"
    },
    "1124": {
        "Type": "",
        "Head": "",
        "Name": "сведения об идентификации товара"
    },
    "1126": {
        "Type": BYTE,
        "Head": "ПРОВЕДЕНИЕ ЛОТЕРЕИ",
        "Name": "признак проведения лотереи"
    },
    "1129": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики операций \"приход\""
    },
    "1130": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики операций \"возврат прихода\""
    },
    "1131": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики операций \"расход\""
    },
    "1132": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики операций \"возврат расхода\""
    },
    "1133": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики операций по чекам коррекции"
    },
    "1134": {
        "Type": INT32,
        "Head": "",
        "Name": "количество чеков со всеми признаками расчетов"
    },
    "1135": {
        "Type": INT32,
        "Head": "",
        "Name": "количество чеков по признаку расчетов"
    },
    "1136": {
        "Type": COINS,
        "Head": "",
        "Name": "итоговая сумма в чеках наличными"
    },
    "1138": {
        "Type": COINS,
        "Head": "",
        "Name": "итоговая сумма в чеках электронными"
    },
    "1139": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма НДС по ставке 20%"
    },
    "1140": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма НДС по ставке 10%"
    },
    "1141": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма НДС по ставке 20/120"
    },
    "1142": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма НДС по ставке 10/110"
    },
    "1143": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма НДС по ставке 0%"
    },
    "1144": {
        "Type": INT32,
        "Head": "",
        "Name": "количество чеков коррекции"
    },
    "1145": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики коррекций \"приход\""
    },
    "1146": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики коррекций \"расход\""
    },
    "1148": {
        "Type": INT32,
        "Head": "",
        "Name": "количество самостоятельных корректировок"
    },
    "1149": {
        "Type": INT32,
        "Head": "",
        "Name": "количество корректировок по предписанию"
    },
    "1151": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма коррекций с НДС по ставке 20%"
    },
    "1152": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма коррекций с НДС по ставке 10%"
    },
    "1153": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма коррекций с НДС по ставке 20/120"
    },
    "1154": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма коррекций с НДС по ставке 10/110"
    },
    "1155": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма коррекций с НДС по ставке 0%"
    },
    "1157": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики итогов ФН"
    },
    "1158": {
        "Type": STLV,
        "Head": "",
        "Name": "счётчики итогов непереданных ФД"
    },
    "1162": {
        "Type": BYTES,
        "Head": "",
        "Name": "код товарной номенклатуры"
    },
    "1171": {
        "Type": STRING,
        "Head": "",
        "Name": "телефон поставщика"
    },
    "1173": {
        "Type": ENUM,
        "Head": "",
        "Name": "тип коррекции",
        "Value0": "самостоятельно",
        "Value1": "по предписанию"
    },
    "1174": {
        "Type": STLV,
        "Head": "",
        "Name": "основание для коррекции"
    },
    "1177": {
        "Type": STRING,
        "Head": "",
        "Name": "наименование основания для коррекции"
    },
    "1178": {
        "Type": UNIXTIME,
        "Head": "",
        "Name": "дата документа основания для коррекции"
    },
    "1179": {
        "Type": STRING,
        "Head": "",
        "Name": "номер документа основания для коррекции"
    },
    "1183": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма расчетов без НДС"
    },
    "1184": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма коррекций без НДС"
    },
    "1187": {
        "Type": STRING,
        "Head": "",
        "Name": "место расчетов"
    },
    "1188": {
        "Type": STRING,
        "Head": "",
        "Name": "версия ККТ"
    },
    "1189": {
        "Type": ENUM,
        "Head": "",
        "Name": "версия ФФД ККТ",
        "Value1": "1.0",
        "Value2": "1.05",
        "Value3": "1.1",
        "Value4": "1.2"
    },
    "1190": {
        "Type": ENUM,
        "Head": "",
        "Name": "версия ФФД ФН",
        "Value1": "1.0",
        "Value2": "1.05",
        "Value3": "1.1",
        "Value4": "1.2"
    },
    "1191": {
        "Type": STRING,
        "Head": "",
        "Name": "дополнительный реквизит предмета расчета"
    },
    "1192": {
        "Type": STRING,
        "Head": "",
        "Name": "дополнительный реквизит чека"
    },
    "1193": {
        "Type": BYTE,
        "Head": "",
        "Name": "признак проведения азартных игр"
    },
    "1194": {
        "Type": STLV,
        "Head": "",
        "Name": "счетчики итогов смены"
    },
    "1197": {
        "Type": STRING,
        "Head": "",
        "Name": "единица измерения предмета расчета"
    },
    "1198": {
        "Type": COINS,
        "Head": "",
        "Name": "размер НДС за единицу предмета расчета",
    },
    "1199": {
        "Type": ENUM,
        "Head": "",
        "Name": "ставка НДС",
        "Value1": "ставка НДС 20%",
        "Value2": "ставка НДС 10%",
        "Value3": "ставка НДС расч. 20/120",
        "Value4": "ставка НДС расч. 10/110",
        "Value5": "ставка НДС 0%",
        "Value6": "НДС не облагается",
    },
    "1200": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма НДС за предмет расчета",
    },
    "1201": {
        "Type": COINS,
        "Head": "",
        "Name": "общая итоговая сумма в чеках",
    },
    "1203": {
        "Type": STRING,
        "Head": "",
        "Name": "ИНН кассира",
    },
    "1205": {
        "Type": INT32,
        "Head": "",
        "Name": "коды причин изменения сведений о ККТ",
    },
    "1206": {
        "Type": BITS,
        "Head": "",
        "Name": "сообщение оператора",
        "BIT1": "ошибка ФЛК",
        "BIT6": "требуется настроить ККТ",
        "BIT7": "ОФД аннулирован",
    },
    "1207": {
        "Type": BYTE,
        "Head": "",
        "Name": "признак торговли подакцизными товарами",
    },
    "1208": {
        "Type": STRING,
        "Head": "",
        "Name": "сайт чеков",
    },
    "1209": {
        "Type": ENUM,
        "Head": "",
        "Name": "версия ФФД",
        "Value1": "1.0",
        "Value2": "1.05",
        "Value3": "1.1",
        "Value4": "1.2",
    },
    "1212": {
        "Type": ENUM,
        "Head": "",
        "Name": "признак предмета расчета",
        "Value1": "товар",
        "Value2": "подакцизный товар",
        "Value3": "работа",
        "Value4": "услуга",
        "Value5": "ставка азартной игры",
        "Value6": "выигрыш азартной игры",
        "Value7": "лотерейный билет",
        "Value8": "выигрыш лотереи",
        "Value9": "предоставление РИД",
        "Value10": "платеж (выплата)",
        "Value11": "агентское вознаграждение",
        "Value12": "составной предмет расчета",
        "Value13": "иной предмет расчета",
        "Value14": "имущественное право",
        "Value15": "внереализационный доход",
        "Value16": "стаховой взнос",
        "Value17": "торговый взнос",
        "Value18": "курортный сбор",
        "Value20": "",
        "Value21": "",
        "Value22": "",
        "Value23": "",
        "Value24": "",
        "Value25": "",
        "Value26": "",
        "Value27": "",
        "Value28": "",
        "Value29": "",
        "Value30": "",
        "Value31": ""
    },
    "1213": {
        "Type": INT16,
        "Head": "",
        "Name": "ресурс ключей ФП"
    },
    "1214": {
        "Type": ENUM,
        "Head": "",
        "Name": "признак способа расчета",
        "Value1": "предоплата 100%",
        "Value2": "предоплата",
        "Value3": "аванс",
        "Value4": "полный расчет",
        "Value5": "частичный расчет и кредит",
        "Value6": "передача в кредит",
        "Value7": "оплата кредита"
    },
    "1215": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма по чеку предоплатой (зачетом аванса)",
    },
    "1216": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма по чеку постоплатой (в кредит)",
    },
    "1217": {
        "Type": COINS,
        "Head": "",
        "Name": "сумма по чеку встречным предоставлением",
    },
    "1218": {
        "Type": COINS,
        "Head": "",
        "Name": "итоговая сумма в чеках предоплатами (авансами)",
    },
    "1219": {
        "Type": COINS,
        "Head": "",
        "Name": "итоговая сумма в чеках постоплатами (кредитами)",
    },
    "1220": {
        "Type": COINS,
        "Head": "",
        "Name": "итоговая сумма в чеках встречными предоставлениями",
    },
    "1221": {
        "Type": BYTE,
        "Head": "",
        "Name": "признак установки принтера в автомате",
    },
    "1222": {
        "Type": BITS,
        "Head": "",
        "Name": "признак агента по предмету расчета",
        "BIT0": "банк. пл. агент",
        "BIT1": "банк. пл. субагент",
        "BIT2": "плат. агент",
        "BIT3": "плат. субагент",
        "BIT4": "поверенный",
        "BIT5": "комиссионер",
        "BIT6": "агент",
    },
    "1223": {
        "Type": STLV,
        "Head": "",
        "Name": "данные агента",
    },
    "1224": {
        "Type": STLV,
        "Head": "",
        "Name": "данные поставщика",
    },
    "1225": {
        "Type": STRING,
        "Head": "",
        "Name": "наименование поставщика",
    },
    "1226": {
        "Type": STRING,
        "Head": "",
        "Name": "ИНН поставщика"
    },
    "1227": {
        "Type": STRING,
        "Head": "",
        "Name": "покупатель (клиент)"
    },
    "1228": {
        "Type": STRING,
        "Head": "",
        "Name": "ИНН покупателя (клиента)"
    },
    "1229": {
        "Type": COINS,
        "Head": "",
        "Name": "акциз"
    },
    "1230": {
        "Type": STRING,
        "Head": "",
        "Name": "код страны происхождения товара"
    },
    "1231": {
        "Type": STRING,
        "Head": "",
        "Name": "номер таможенной декларации"
    },
    "1232": {
        "Type": STLV,
        "Head": "",
        "Name": "счетчики по признаку \"возврат прихода\""
    },
    "1233": {
        "Type": STLV,
        "Head": "",
        "Name": "счетчики по признаку \"возврат расхода\""
    },
    "1257": {
        "Type": BYTE,
        "Head": "",
        "Name": "признак осуществления ломбардной деятельности"
    },
    "1258": {
        "Type": BYTE,
        "Head": "",
        "Name": "признак осуществления страховой деятельности"
    },
    "1290": {
        "Type": BITS,
        "Head": "",
        "Name": "признаки условий применения ККТ",
        "BIT1": "ПРИНТЕР В АВТОМАТЕ",
        "BIT2": "АС БСО",
        "BIT5": "ККТ ДЛЯ ИНТЕРНЕТ",
        "BIT6": "ПОДАКЦИЗНЫЕ ТОВАРЫ",
        "BIT8": "ТМТ",
        "BIT9": "ККТ ДЛЯ УСЛУГ",
        "BIT10": "ПРОВЕДЕНИЕ АЗАРТНОЙ ИГРЫ",
        "BIT11": "ПРОВЕДЕНИЕ ЛОТЕРЕИ",
        "BIT12": "ЛОМБАРД",
        "BIT13": "СТРАХОВАНИЕ"
    },
    "2000": {
        "Type": STRING,
        "Head": "",
        "Name": "код маркировки"
    },
    "2007": {
        "Type": COINS,
        "Head": "",
        "Name": "данные о маркированном товаре"
    },
    "2100": {
        "Type": BYTE,
        "Head": "",
        "Name": "тип кода маркировки"
    },
    "2101": {
        "Type": STRING,
        "Head": "",
        "Name": "код идентификации товара"
    },
    "2102": {
        "Type": BYTE,
        "Head": "",
        "Name": "режим обработки кода маркировки",
    },
    "2103": {
        "Type": BYTE,
        "Head": "",
        "Name": "признак торговли маркированными товарами",
    },
    "2106": {
        "Type": BYTE,
        "Head": "",
        "Name": "результат проверки сведений о товаре",
    },
    "2110": {
        "Type": BYTE,
        "Head": "",
        "Name": "присвоенный статус товара",
    },
    "2115": {
        "Type": STRING,
        "Head": "",
        "Name": "код идентификации вида товара",
    },
    "2117": {
        "Type": COINS,
        "Head": "",
        "Name": "отраслевой реквизит чека",
    },
    "65001": {
        "Type": STLV,
        "Head": "",
        "Name": "ФДн в автономном режиме для ФФД 1.0 и 1.05",
    },
    "65002": {
        "Type": STLV,
        "Head": "",
        "Name": "ФДн и подтверждение для ФФД 1.0 и 1.05",
    },
    "65011": {
        "Type": STLV,
        "Head": "",
        "Name": "ФДн в автономном режиме для ФФД ФФД 1.1",
    },
    "65012": {
        "Type": STLV,
        "Head": "",
        "Name": "ФДн и подтверждение для ФФД 1.1",
    },
    "fiscalDocumentType": {
        "Type": STRING,
        "Head": "",
        "Name": "Тип документа",
    },
    "qr": {
        "Type": STRING,
        "Head": "",
        "Name": "QR код чека 1196",
    },
    "short": {
        "Type": STRING,
        "Head": "",
        "Name": "Признак того, что документ считался из архива и содержит неполный набор данных",
    },

}
