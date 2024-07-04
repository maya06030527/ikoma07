import streamlit as st

def calculate_points(feedback):
    if feedback == "できた":
        return 5
    elif feedback == "がんばろう":
        return 0

def main():
    st.markdown("<h1 style='text-align: center;'>DEKITA!を増やそう</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>小学生のための</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>生活習慣改善応援アプリ（低学年向け）</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; color: purple;'>あさ</h1>", unsafe_allow_html=True)

    # プルダウンサイドバーに表示させる
    hayaoki = st.selectbox('◆6じ30ぷんにおきる', ('できた', 'がんばろう'))
    kaoarai = st.selectbox('◆かおあらい・ねぐせなおし', ('できた', 'がんばろう'))
    osara = st.selectbox('◆おさらかたづけ', ('できた', 'がんばろう'))
    hamigaki = st.selectbox('◆はみがき', ('できた', 'がんばろう'))
    motimono = st.selectbox('◆もちものかくにん', ('できた', 'がんばろう'))
    pajama = st.selectbox('◆パジャマかたづけ', ('できた', 'がんばろう'))
    syuppatu = st.selectbox('◆７じ３０ぷんまでにしゅっぱつ', ('できた', 'がんばろう'))

    st.markdown("<h1 style='text-align: left; color: purple;'>よる</h1>", unsafe_allow_html=True)
    kutusoroe = st.selectbox('◆くつそろえ', ('できた', 'がんばろう'))
    araimono = st.selectbox('◆あらいもの・プリントをすぐだす', ('できた', 'がんばろう'))
    shukudai = st.selectbox('◆しゅくだい', ('できた', 'がんばろう'))
    piano = st.selectbox('◆ピアノ', ('できた', 'がんばろう'))
    challenge = st.selectbox('◆とくべつチャレンジ（てつぼう・じてんしゃ・ふっきんなど）', ('できた', 'がんばろう'))
    otetsudai = st.selectbox('◆おてつだいチャレンジ', ('できた', 'がんばろう'))
    omocha = st.selectbox('◆おもちゃかたづけ', ('できた', 'がんばろう'))
    ashitayoi = st.selectbox('◆あしたのようい', ('できた', 'がんばろう'))

    # 各タスクのポイント計算
    points_hayaoki = calculate_points(hayaoki)
    points_kaoarai = calculate_points(kaoarai)
    points_osara = calculate_points(osara)
    points_hamigaki = calculate_points(hamigaki)
    points_motimono = calculate_points(motimono)
    points_pajama = calculate_points(pajama)
    points_syuppatu = calculate_points(syuppatu)
    points_kutusoroe = calculate_points(kutusoroe)
    points_araimono = calculate_points(araimono)
    points_shukudai = calculate_points(shukudai)
    points_piano = calculate_points(piano)
    points_challenge = calculate_points(challenge)
    points_otetsudai = calculate_points(otetsudai)
    points_omocha = calculate_points(omocha)
    points_ashitayoi = calculate_points(ashitayoi)

    # 合計ポイント計算
    total_points = (
        points_hayaoki + points_kaoarai + points_osara +
        points_hamigaki + points_motimono + points_pajama +
        points_syuppatu + points_kutusoroe + points_araimono +
        points_shukudai + points_piano + points_challenge +
        points_otetsudai + points_omocha + points_ashitayoi
    )

    st.title("おつかれさま！")
    # 合計ポイントの表示を大きくする
    st.markdown(f"<h1 style='text-align: left; color: green;'>合計ポイント: {total_points} ポイント</h1>", unsafe_allow_html=True)

    # ポイントに応じたメッセージを左揃えで大きく表示
    st.markdown(f"<h3 style='text-align: left; color: blue;'>今日のYouTube・ゲームのじかんは {total_points} 分★</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: left; color: blue;'>らいげつのおこづかい {total_points} 円アップ★</h3>", unsafe_allow_html=True)

    # 満点時に風船を表示し、メッセージを左揃えで表示
    if total_points == 75:
        st.balloons()
        st.markdown("<h1 style='text-align: left; color: gold;'>満点おめでとう！</h1>", unsafe_allow_html=True)
    elif 50 <= total_points <= 70:
        st.markdown("<h1 style='text-align: left; color: red;'>よくがんばってるね！</h1>", unsafe_allow_html=True)

  # あしたもいっしょにがんばろう☆ の表示
    st.markdown("<h2 style='text-align: left;'>あしたもいっしょにがんばろう☆</h2>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()