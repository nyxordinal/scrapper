import csv

fileUrl="nice.csv"
file=open(fileUrl)
mycsv = csv.reader(file)

header = []
header = next(mycsv)
drugs = []

lim=3000

for idx, row in enumerate(mycsv):
    drug = {
        "id":idx+1,
        'name': row[1],
        'b_capital_price': row[6],
        'b_price': row[6],
        'b_cvt_amount': row[2],
        'b_qty': row[3],
        'no_batch': row[4],
        'expire': row[5],
    }
    drugs.append(drug)
    if idx+1==lim:
            break


def generate_product_lines(offset,limit):
    query=""
    n=1
    for idx, d in enumerate(drugs):
        if idx+1>offset:
            query+=f"   (2, '{d['name']}', '', NOW(), NOW())"
            if n == limit:
                query+=";"
                break
            else:
                query+=",\n"
                n+=1

    f = open("import.sql", "w")
    f.write('INSERT INTO product_lines (apotek_id, name, description, created_at, updated_at)\n')
    f.write('VALUES\n')
    f.write(query)
    f.close()

   
    
def generate_products(offset, limit):
    query=""
    n=1
    for idx, d in enumerate(drugs):
        if idx+1>offset:
            if d['no_batch']!='' and d['expire']!='':
                cvt_amount = d['b_cvt_amount']
                if cvt_amount=='':
                    cvt_amount=0 
                query+=f"   ('{d['no_batch']}', {d['id']}, 2, {d['b_qty']}, {d['b_price']}, {d['b_capital_price']}, {cvt_amount}, CAST('{d['expire']}' AS DATE), NOW(), NOW()),\n"
            if n == limit:
                break
            n+=1
    
    f = open("import_products.sql", "w")
    f.write('INSERT INTO products (batch_number, product_line_id, apotek_id, b_qty, b_price, b_capital_price, b_cvt_amount, expire_date, created_at, updated_at)\n')
    f.write('VALUES\n')
    f.write(query)
    f.close()
    
generate_product_lines(offset=1500,limit=1000)
generate_products(offset=1500,limit=1000)

file.close()
# offset id 20