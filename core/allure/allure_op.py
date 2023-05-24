import json
import allure


def attach_compare_results(result: dict, name: str):
    # json_string = json.dumps(result, indent=4, )
    # result = json_string.encode('utf-8').decode('unicode_escape')
    lines = []
    for key, value in result.items():
        if len(value) < 6:
            continue
        _, status, code, compared, etalon, message = value
        line = f"{status} | {code} | etalon {etalon} | compared {compared} | {message}"
        lines.append(line)
    report = "\n".join(lines)
    allure.attach(report, name=name, attachment_type=allure.attachment_type.TEXT)



# {
#     "1": [
#         true,
#         "+++PASS+++",
#         "1018",
#         "112233445573",
#         "112233445573",
#         "\u0418\u041d\u041d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f"
#     ],

