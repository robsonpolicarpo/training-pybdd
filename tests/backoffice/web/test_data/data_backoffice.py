import logging

from tests.backoffice.web.support.enuns.filepath_enum import FilePath
from tests.support.csv_util import read_like_dict
from tests.support.csv_util import write_csv_str
from tests.support.faker_data import FakerData


class DataB2BAdmin(FakerData):

    def generate_products_csv(self, filepath, qty=2):
        data = []
        prods = self.get_prods_filtered()
        for _ in range(qty):
            random_index = self.faker.random.randint(0, len(prods) - 1)
            prod = prods[random_index]
            data.append(f"{prod['sku']};{prod['packing_size']};77620588000100")
        write_csv_str(filepath, data)
        return data

    @staticmethod
    def get_prods_filtered():
        all_prods_api = read_like_dict(FilePath.PRODS_API_QABOT.value)
        prods_actives = [prod for prod in all_prods_api if prod['status'] == 'A']
        prods_with_inventory = []
        qty_min_prod_on_inventory = 4
        for prod in prods_actives:
            try:
                qty_prod_on_inventory = int(prod['inventory'])
                if qty_prod_on_inventory > qty_min_prod_on_inventory:
                    prods_with_inventory.append(prod)
            except Exception as e:
                logging.warning(e)
        return prods_with_inventory
