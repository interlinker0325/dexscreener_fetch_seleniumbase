from seleniumbase import SB
import json

with SB(uc=True) as sb:
    url = "https://example.com"
    sb.uc_open_with_reconnect(url, 4)
    sb.uc_gui_click_captcha()
    sb.sleep(3)
    elements = sb.find_element("css selector", "div.ds-dex-table-top")
    # print(elements, "elements")
    rows = elements.find_elements("css selector", "a.ds-dex-table-row-top")
    # print(rows, "rows")
    token = []
    for row in rows:
        token_infors = row.find_element("css selector", "div.ds-dex-table-row-col-token")
        # print(token_infors, "token_infors")
        token_symbol = token_infors.find_element("css selector", "span.ds-dex-table-row-base-token-symbol").text
        token_name = token_infors.find_element("css selector", "div.ds-dex-table-row-base-token-name").find_element("css selector", "span").text
        token_price = row.find_element("css selector", "div.ds-dex-table-row-col-price").text
        token_volume = row.find_element("css selector", "div.ds-dex-table-row-col-volume").text
        token.append({
            "token_symbol": token_symbol,
            "token_name": token_name,
            "token_price": token_price,
            "token_volume": token_volume
        })
with open("dexscreener.json", "w", encoding="utf-8") as f:
    json.dump(token, f, ensure_ascii=False, indent=4)
sb.sleep(2)

