@app.route('/order', methods=['GET'])
def order():
    #
    lock_prod_sql="select quantity from HOTDEAL_LIST where PROD_ID = 1 for update"
    rs = cursor.execute(lock_prod_sql)
    for record in rs:
        currVal = record[0]
        if(currVal > 0):
            currVal = currVal - 1;
            decreaseQuantitySQL = "update HOTDEAL_LIST set quantity="+str(currVal)+" where PROD_ID=1"
            cursor.execute(decreaseQauntitySQL);
            orderInsertSQL = "insert into ORDER_HISTORY values (sysdate, CUST_ID,1)"
            cursor.execute(orderInsertSQL);
            PAYMENT_PROCESS(CUST_ID,PRICE)
            conn.commit()
        else:
            return render_template(
                'OutOfStock.html',
                pMessage="Out of Stock"
            )

    cursor.close()
    conn.close()
    return "Completed"

