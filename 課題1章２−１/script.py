all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    #ここから記述（ヒント：in演算子を用いて、条件分岐）
    if place == "札幌":
        print(place + "のチケットは結果待ち")
    #ここから記述（ヒント：in演算子を用いて、条件分岐
    elif place == "東京":
        print(place + "のチケットは落選しました")
    elif place == "横浜":
        print( place+ "のチケットが当選しました")
    elif place == "大阪":
        print(place + "のチケットは結果待ち")
    elif place == "名古屋":
        print(place + "のチケットは落選しました")
    elif place == "福岡":
        print(place + "のチケットは落選しました")
        #科第２−２
    elif place == "横浜" "札幌" "大阪":
        print(place + "横浜と札幌と大阪のチケットが当選しました")


    else:
        print(place + "のチケットは落選しました")

