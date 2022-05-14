@app.route('/order-redis', methods=['GET'])
def order_redis():
    # REDIS에서 PRD_001_QTY를 통해 남은 수량 확인
    currVal = int(r.get('PRD_001_QTY'))
    # 남은 수량이 있을 경우 ORDER를 성공, 실패시 OutOfStock.html을 return
    if(currVal > 0):
        r.decr('PRD_001_QTY',1)
        orderInsertSQL = "insert into ORDER_HISTORY values (sysdate, CUST_ID,1)"
        cursor.execute(orderInsertSQL);
        PAYMENT_PROCESS(CUST_ID, PRICE)
        conn.commit()
    else:
        return render_template(
            'OutOfStock.html',
            pMessage="Out of Stock"
        )

    cursor.close()
    conn.close()
    return "Completed"

