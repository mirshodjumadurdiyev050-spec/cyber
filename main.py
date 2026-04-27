import streamlit as st
import streamlit.components.v1 as components
from logic import classical, rsa, hashing, pdf_gen
import ast
import time
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Cryptographic Lab - Professional Crypto Tools",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Meta tags for SEO
st.markdown("""
    <head>
        <meta name="description" content="Professional Cryptographic Laboratory - Learn Caesar, Vigenere, RSA, and SHA-256 with interactive visualizations and academic PDF guides.">
        <meta name="keywords" content="Cryptography, RSA, Vigenere, Caesar, Hash, SHA-256, Security, Education, Uzbekistan">
        <meta name="author" content="Crypt Lab Team">
    </head>
""", unsafe_allow_html=True)

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/styles.css")

# Session State Initialization
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Navigation Function
def set_page(name):
    st.session_state.page = name

# Custom Header (HTML)
def render_header():
    # Light Modern Nav Bar
    st.markdown("""
        <div class="top-nav" style="background: rgba(255, 255, 255, 0.7); border-bottom: 1px solid rgba(0,0,0,0.05); backdrop-filter: blur(15px);">
            <div class="nav-brand" style="color: #1a1a1a;">
                <i class="fa-solid fa-shield-halved" style="color: #6366f1;"></i> 
                <span style="font-weight: 800; letter-spacing: 1px;">CRYPT LAB</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns([2.5, 0.8, 0.8, 0.8, 0.8, 1, 2.5])
    nav_items = [
        ("Asosiy", "Home", "nav_home"),
        ("Klassik", "Classical", "nav_classic"),
        ("RSA", "RSA", "nav_rsa"),
        ("Xesh", "Hash", "nav_hash"),
        ("Kutubxona", "Library", "nav_lib")
    ]
    for i, (label, page, key) in enumerate(nav_items):
        with cols[i+1]:
            if st.button(label, key=key, use_container_width=True):
                set_page(page)

def render_home():
    # Enhanced Hero Section (Fixed Indentation)
    st.markdown("""
<div class="glass-card fade-in" style="padding: 5rem 2rem; text-align: center; background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.05), transparent), radial-gradient(circle at bottom left, rgba(16, 185, 129, 0.05), transparent), rgba(255,255,255,0.9); border: 1px solid white; box-shadow: 0 40px 80px rgba(0,0,0,0.03); margin-bottom: 3rem; position: relative; overflow: hidden; border-radius: 40px;">
<div style="position: absolute; top: -100px; right: -100px; width: 300px; height: 300px; background: rgba(99, 102, 241, 0.08); border-radius: 50%; filter: blur(60px);"></div>
<div style="position: absolute; bottom: -100px; left: -100px; width: 300px; height: 300px; background: rgba(16, 185, 129, 0.08); border-radius: 50%; filter: blur(60px);"></div>
<h1 style="font-size: 4.5rem; font-weight: 950; line-height: 1; margin-bottom: 1.5rem; letter-spacing: -2px;">
<span style="background: linear-gradient(135deg, #6366f1, #4f46e5); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">KRIPTO</span> 
<span style="background: linear-gradient(135deg, #333, #888); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">LABORATORIYA</span>
</h1>
<p style="font-size: 1.5rem; color: #444; max-width: 800px; margin: 0 auto 3rem; line-height: 1.6; font-weight: 400;">
Akademik tadqiqotlar va xavfsiz ma'lumotlar almashinuvi uchun mo'ljallangan <br>
<span style="color: #6366f1; font-weight: 700; border: 1px solid #6366f1; padding: 2px 15px; border-radius: 50px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">V2.0 Professional Edition</span>
</p>
<div style="display: flex; justify-content: center; gap: 1.5rem; align-items: center;">
<div style="padding: 1.2rem 3rem; background: linear-gradient(135deg, #6366f1, #4f46e5); color: white; border-radius: 20px; font-weight: 800; font-size: 1.1rem; box-shadow: 0 20px 40px rgba(99, 102, 241, 0.3); cursor: pointer; transform: perspective(1px) translateZ(0); transition: all 0.3s ease;">
Ishni Boshlash
</div>
<div style="padding: 1.2rem 3rem; border: 2px solid #e2e8f0; color: #1e293b; border-radius: 20px; font-weight: 700; font-size: 1.1rem; background: white; transition: all 0.3s ease;">
Tizim Holati
</div>
</div>
<div style="margin-top: 3rem; display: flex; justify-content: center; gap: 2rem; color: #94a3b8; font-size: 0.9rem;">
<span><i class="fa-solid fa-check-circle" style="color: #10b981;"></i> 100% Xavfsiz</span>
<span><i class="fa-solid fa-check-circle" style="color: #10b981;"></i> Akademik Daraja</span>
<span><i class="fa-solid fa-check-circle" style="color: #10b981;"></i> Ochiq Manba</span>
</div>
</div>
""", unsafe_allow_html=True)
    
    # Dashboard Stats
    cols = st.columns(4)
    stats = [
        {"icon": "fa-microchip", "label": "Tizim Quvvati", "val": "99.9%", "color": "#10b981"},
        {"icon": "fa-shield-halved", "label": "Himoya", "val": "AES-256", "color": "#6366f1"},
        {"icon": "fa-bolt", "label": "Tezlik", "val": "1.2 ms", "color": "#f59e0b"},
        {"icon": "fa-user-shield", "label": "Seans", "val": "Xavfsiz", "color": "#ef4444"}
    ]
    
    for i, stat in enumerate(stats):
        with cols[i]:
            st.markdown(f"""
                <div class="glass-card fade-in" style="text-align: center; padding: 1.5rem; border-bottom: 4px solid {stat['color']}; transition: transform 0.3s ease;">
                    <i class="fa-solid {stat['icon']}" style="font-size: 2rem; color: {stat['color']}; margin-bottom: 1rem;"></i>
                    <div style="font-size: 0.8rem; color: #888; text-transform: uppercase; letter-spacing: 1px;">{stat['label']}</div>
                    <div style="font-size: 1.4rem; font-weight: 800; color: #1a1a1a;">{stat['val']}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("""
        <div class="banner fade-in" style="margin-top: 2rem; padding: 1rem; background: rgba(0,0,0,0.02); border-radius: 12px; display: flex; align-items: center; gap: 15px;">
            <i class="fa-solid fa-graduation-cap" style="font-size: 1.2rem; color: #333;"></i>
            <div>
                <span style="font-weight: 700;">YANGILIK:</span> 
                Akademik darajadagi PDF qo'llanmalar va chuqurlashtirilgan nazariya qo'shildi!
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_classical():
    st.markdown('<div class="glass-card fade-in"><h2><i class="fa-solid fa-feather"></i> Klassik Shifrlar</h2></div>', unsafe_allow_html=True)
    
    tabs = st.tabs(["Sezar Shifri", "Vigenere Shifri", "Vernam Shifri"])
    
    with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            text = st.text_area("Ma'lumot", placeholder="Matnni kiriting...", key="caesar_input")
            shift = st.slider("Siljish (Shift)", 1, 25, 3)
        with col2:
            mode = st.radio("Amal", ["Shifrlash", "Deshifrlash"], key="caesar_mode")
            if text:
                m = 'encrypt' if mode == "Shifrlash" else 'decrypt'
                res = classical.caesar_cipher(text, shift, m)
                render_result("Natija", res)
                
                if st.button("🔄 Natijani matnga ko'chirish (Deshifrlash uchun)", key="copy_caesar"):
                    st.session_state.caesar_input = res
                    st.rerun()
                
                # Sezar vizualizatsiyasi
                st.write("---")
                st.subheader("📊 Alifbo siljishi")
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                shifted = alphabet[shift:] + alphabet[:shift]
                
                header_c = "".join([f"<th style='border: 1px solid var(--glass-border); padding: 5px; font-size: 0.7rem; background: rgba(255,255,255,0.05);'>{c}</th>" for c in alphabet])
                cells_c = "".join([f"<td style='border: 1px solid var(--glass-border); padding: 5px; font-size: 0.7rem;'>{c}</td>" for c in shifted])
                
                st.markdown(f"""
                    <div class="glass-card fade-in" style="overflow-x: auto; padding: 1.5rem;">
                        <table style="width: 100%; border-collapse: collapse; font-family: 'JetBrains Mono', monospace; color: white; text-align: center;">
                            <tr>
                                <th style="border: 1px solid var(--glass-border); padding: 5px; background: rgba(255,255,255,0.1);">Asl</th>
                                {header_c}
                            </tr>
                            <tr>
                                <td style="border: 1px solid var(--glass-border); padding: 5px; font-weight: bold; background: rgba(255,255,255,0.05);">Shifr (k={shift})</td>
                                {cells_c}
                            </tr>
                        </table>
                    </div>
                """, unsafe_allow_html=True)

    with tabs[1]:
        # Boshlovchilar uchun qo'llanma
        with st.expander("❓ Bu nima va qanday ishlatiladi? (Yangi o'rganuvchilar uchun)", expanded=True):
            col_a, col_b = st.columns([1, 2])
            with col_a:
                st.markdown("### 🔒 Vijiner Shifri")
            with col_b:
                st.write("""
                Bu usul — xabarlaringizni faqat kalit so'zni bilgan odam o'qiy oladigan **"maxfiy til"**ga aylantiradi.
                
                **Qanday ishlatish kerak?**
                1. **Ma'lumot:** Yashirmoqchi bo'lgan xabaringizni yozing (Masalan: *SALOM*).
                2. **Kalit so'z:** Uni yashirish uchun birorta so'z o'ylab toping (Masalan: *OLMA*).
                3. **Natija:** Pastdagi jadvallar sizga bu so'zlar qanday qilib maxfiy kodga aylanganini ko'rsatadi.
                """)
                if st.button("Ko'rish uchun misol to'ldirish"):
                    st.session_state.vigenere_input = "JUMADURDIYEV"
                    st.session_state.vigenere_key = "MIRSHOD"
                    st.rerun()

        col1, col2 = st.columns(2)
        with col1:
            v_text = st.text_area("Ma'lumot", placeholder="Matnni kiriting...", key="vigenere_input")
            v_key = st.text_input("Kalit so'z", placeholder="Masalan: SECRET", key="vigenere_key")
        with col2:
            v_mode = st.radio("Amal", ["Shifrlash", "Deshifrlash"], key="vigenere_mode")
            if v_text and v_key:
                m = 'encrypt' if v_mode == "Shifrlash" else 'decrypt'
                res = classical.vigenere_cipher(v_text, v_key, m)
                render_result("Natija", res)
                
                if st.button("🔄 Natijani matnga ko'chirish (Deshifrlash uchun)", use_container_width=True):
                    st.session_state.vigenere_input = res
                    st.rerun()
                
                # Vizual jadval yaratish (Rasmdagidek)
                st.write("---")
                st.subheader("📊 Qadamma-qadam vizualizatsiya")
                
                anim_col1, anim_col2 = st.columns([1, 2])
                with anim_col1:
                    start_anim = st.button("🚀 Jonli Animatsiyani Ko'rish", key="v_anim_btn")
                
                placeholder = st.empty()
                
                def render_vigenere_visuals(focus_idx=None):
                    # Matn va kalitni tayyorlash
                    v_text_clean = [c for c in v_text if c.isalpha()]
                    if not v_text_clean: return
                    
                    v_key_repeated = [v_key[i % len(v_key)].upper() for i in range(len(v_text_clean))]
                    v_res_clean = [c for c in res if c.isalpha()]
                    
                    # --- 2.2-jadval: Vijiner usulida shifrlash (Alifbo siljishlari) ---
                    unique_key_chars = []
                    for char in v_key.upper():
                        if char.isalpha() and char not in unique_key_chars:
                            unique_key_chars.append(char)
                    
                    # Palette
                    palette = ["#ff4b4b", "#4bff4b", "#4b4bff", "#ffff4b", "#ff4bff", "#4bffff", "#ff9f4b"]
                    
                    # Intersections mapping
                    intersections = {}
                    row_highlights = {}
                    col_highlights = {}
                    
                    # If focusing on one char, only highlight that one
                    range_to_draw = range(len(v_text_clean)) if focus_idx is None else [focus_idx]
                    
                    for i in range_to_draw:
                        p_c = v_text_clean[i].upper()
                        k_c = v_key_repeated[i].upper()
                        color = palette[i % len(palette)]
                        intersections[(k_c, p_c)] = color
                        if k_c not in row_highlights: row_highlights[k_c] = []
                        row_highlights[k_c].append(color)
                        if p_c not in col_highlights: col_highlights[p_c] = []
                        col_highlights[p_c].append(color)

                    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    def get_shifted_alphabet(char):
                        shift = ord(char) - ord('A')
                        return alphabet[shift:] + alphabet[:shift]

                    # Header
                    header_2_2 = ""
                    for c in alphabet:
                        h_colors = col_highlights.get(c, [])
                        style = ""
                        if h_colors:
                            style = f"background: {h_colors[0]}33; color: {h_colors[0]}; font-weight: bold; border-bottom: 3px solid {h_colors[0]};"
                        header_2_2 += f"<th style='border: 1px solid var(--glass-border); padding: 5px; font-size: 0.7rem; background: rgba(255,255,255,0.05); {style}'>{c}</th>"
                    
                    rows_2_2 = ""
                    unique_key_chars = []
                    for char in v_key.upper():
                        if char.isalpha() and char not in unique_key_chars:
                            unique_key_chars.append(char)
                    
                    for char in unique_key_chars:
                        shifted = get_shifted_alphabet(char)
                        r_colors = row_highlights.get(char, [])
                        cells = ""
                        for idx, c in enumerate(shifted):
                            col_char = alphabet[idx]
                            color = intersections.get((char, col_char))
                            style = f"color: white; font-weight: bold; background: {color}; box-shadow: 0 0 8px {color};" if color else ""
                            if not style:
                                r_c = r_colors[0] if r_colors else None
                                c_c = col_highlights.get(col_char, [None])[0]
                                if r_c or c_c: style = f"background: {(r_c if r_c else c_c)}11;"
                            cells += f"<td style='border: 1px solid var(--glass-border); padding: 5px; font-size: 0.7rem; {style}'>{c}</td>"
                        
                        row_style = f"background: {r_colors[0]}33; color: {r_colors[0]}; border-right: 3px solid {r_colors[0]};" if r_colors else ""
                        rows_2_2 += f"<tr><td style='border: 1px solid var(--glass-border); padding: 5px; font-weight: bold; background: rgba(255,255,255,0.05); {row_style}'>{char}</td>{cells}</tr>"

                    # Build output
                    html = f"""
                        <div class="glass-card fade-in" style="overflow-x: auto; padding: 1.5rem; margin-bottom: 1rem;">
                            <h4 style="text-align: center; margin-bottom: 1rem; color: var(--text-secondary);">2.2-jadval. Vijiner usulida shifrlash ({"Jonli Jarayon" if focus_idx is not None else "Rangli xarita"})</h4>
                            <table style="width: 100%; border-collapse: collapse; font-family: 'JetBrains Mono', monospace; color: #333; text-align: center;">
                                <tr><th style="border: 1px solid var(--glass-border); padding: 5px; background: rgba(255,255,255,0.1);"></th>{header_2_2}</tr>
                                {rows_2_2}
                            </table>
                        </div>
                    """
                    
                    # 2.3-jadval
                    res_cells = []
                    for i, c in enumerate(v_res_clean):
                        color = palette[i % len(palette)]
                        opacity = "1" if (focus_idx is None or i <= focus_idx) else "0.1"
                        res_cells.append(f"<td style='border: 1px solid var(--glass-border); padding: 10px; text-align: center; font-weight: bold; color: {color}; background: {color}11; opacity: {opacity};'>{c.upper()}</td>")
                    
                    html += f"""
                        <div class="glass-card fade-in" style="overflow-x: auto; padding: 1.5rem;">
                            <h4 style="text-align: center; margin-bottom: 1rem; color: var(--text-secondary);">2.3-jadval. Vijiner usulida kalit va shifrmatn</h4>
                            <table style="width: 100%; border-collapse: collapse; font-family: 'JetBrains Mono', monospace; color: #333;">
                                <tr><th style="border: 1px solid var(--glass-border); padding: 10px; text-align: left; background: rgba(255,255,255,0.05); width: 150px;">Ochiq matn</th>{"".join([f"<th style='border: 1px solid var(--glass-border); padding: 10px; text-align: center; background: rgba(255,255,255,0.05); opacity: {'1' if (focus_idx is None or i <= focus_idx) else '0.1'};'>{c.upper()}</th>" for i, c in enumerate(v_text_clean)])}</tr>
                                <tr><td style="border: 1px solid var(--glass-border); padding: 10px; text-align: left; background: rgba(255,255,255,0.02);">Kalit</td>{"".join([f"<td style='border: 1px solid var(--glass-border); padding: 10px; text-align: center; opacity: {'1' if (focus_idx is None or i <= focus_idx) else '0.1'};'>{c}</td>" for i, c in enumerate(v_key_repeated)])}</tr>
                                <tr><td style="border: 1px solid var(--glass-border); padding: 10px; text-align: left; background: rgba(255,255,255,0.02);">Shifrlangan matn</td>{"".join(res_cells)}</tr>
                            </table>
                        </div>
                    """
                    
                    if focus_idx is not None:
                        cur_p = v_text_clean[focus_idx].upper()
                        cur_k = v_key_repeated[focus_idx].upper()
                        cur_r = v_res_clean[focus_idx].upper()
                        html += f"""
                        <div class="glass-card fade-in" style="margin-top: 1rem; border-left: 5px solid {palette[focus_idx % len(palette)]}; padding: 1rem;">
                            <b>Hozirgi qadam ({focus_idx + 1}):</b> <br>
                            Ochiq matn harfi: <b>{cur_p}</b> + Kalit harfi: <b>{cur_k}</b> = Natija: <b style="color:{palette[focus_idx % len(palette)]};">{cur_r}</b>
                        </div>
                        """
                    
                    placeholder.markdown(html, unsafe_allow_html=True)

                if start_anim:
                    v_text_clean = [c for c in v_text if c.isalpha()]
                    import time
                    for i in range(len(v_text_clean)):
                        render_vigenere_visuals(focus_idx=i)
                        time.sleep(0.8)
                    render_vigenere_visuals(focus_idx=None) # Final state
                else:
                    render_vigenere_visuals(focus_idx=None)
                st.info("💡 Yuqoridagi jadvallar siz yuborgan rasmdagi 2.2 va 2.3-jadvallarga muvofiq dinamik ravishda generatsiya qilindi.")

                # --- Soddalashtirilgan tushuntirish (Mode-aware) ---
                is_encrypt = (v_mode == "Shifrlash")
                title = "👶 Oddiy tushuntirish (Shifrlash)" if is_encrypt else "🔓 Oddiy tushuntirish (Deshifrlash)"
                
                steps_html = f"""
                    <li style="margin-bottom: 15px;">
                        <b>1. Tepadan qarang:</b> Ochiq matn harfini eng tepadagi qizil qatordan toping.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>2. Yon tomondan qarang:</b> Kalit harfini chap tomondagi qizil ustundan toping.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>3. Natija:</b> Ikkisi uchrashgan joydagi harf — shifr bo'ladi!
                    </li>
                """ if is_encrypt else f"""
                    <li style="margin-bottom: 15px;">
                        <b>1. Yon tomondan boshlang:</b> Kalit harfini chap tomondagi ustundan toping.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>2. Qatordan qidiring:</b> Shu qator bo'ylab yurib, shifrlangan harfni toping.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>3. Tepaga chiqing:</b> Shu harfning tepasidagi eng birinchi harf — bu sizning asl harfingiz!
                    </li>
                """

                st.markdown(f"""
                    <div class="glass-card fade-in" style="margin-top: 2rem; border-left: 4px solid #ff4b4b;">
                        <h3 style="color: #ff4b4b;">{title}</h3>
                        <p style="font-size: 1.1rem; line-height: 1.6;">
                            Bu jarayon juda oddiy:
                        </p>
                        <ul style="list-style-type: none; padding-left: 0;">
                            {steps_html}
                        </ul>
                        <p style="background: rgba(255,75,75,0.1); padding: 15px; border-radius: 8px; border: 1px dashed #ff4b4b;">
                            <b>Hozirgi holatda:</b> <br>
                            {"Shifrlashda biz harflarni birlashtiramiz." if is_encrypt else "Deshifrlashda biz jadvaldan harfni topib, uning 'egasi' (tepadagi harf)ni qidiramiz."}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

    with tabs[2]:
        col1, col2 = st.columns(2)
        with col1:
            ver_text = st.text_area("Ma'lumot", placeholder="Matnni kiriting...", key="vernam_input")
            ver_key = st.text_input("Kalit", placeholder="Masalan: KEY", key="vernam_key")
        with col2:
            st.info("Vernam (XOR) shifri bit darajasida ishlaydi. Shifrlash va deshifrlash amali bir xil.")
            if ver_text and ver_key:
                res = classical.vernam_cipher(ver_text, ver_key)
                render_result("Natija (XOR)", res)
                
                if st.button("🔄 Natijani matnga ko'chirish (Deshifrlash uchun)", key="copy_vernam"):
                    st.session_state.vernam_input = res
                    st.rerun()
                
                # Vernam vizualizatsiyasi (Bitwise XOR)
                st.write("---")
                st.subheader("🔢 Bitwise XOR Vizualizatsiyasi")
                
                rows_v = ""
                # Faqat birinchi 5 ta harfni ko'rsatamiz (agar matn uzun bo'lsa)
                display_len = min(len(ver_text), 5)
                
                for i in range(display_len):
                    char = ver_text[i]
                    k_char = ver_key[i % len(ver_key)]
                    res_char = res[i]
                    
                    b_char = format(ord(char), '08b')
                    b_key = format(ord(k_char), '08b')
                    b_res = format(ord(res_char), '08b')
                    
                    rows_v += f"""
                    <div style="display: flex; justify-content: space-around; align-items: center; background: rgba(0,0,0,0.02); padding: 15px; border-radius: 15px; margin-bottom: 12px; border: 1px solid rgba(0,0,0,0.05); position: relative;">
                        <div style="text-align: center;">
                            <div style="font-size: 0.7rem; color: #888; text-transform: uppercase;">Matn ('{char}')</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; color: #6366f1; letter-spacing: 2px;">{b_char}</div>
                        </div>
                        <div style="font-weight: 900; color: #94a3b8; font-size: 1.2rem;">⊕</div>
                        <div style="text-align: center;">
                            <div style="font-size: 0.7rem; color: #888; text-transform: uppercase;">Kalit ('{k_char}')</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; color: #334155; letter-spacing: 2px;">{b_key}</div>
                        </div>
                        <div style="font-weight: 900; color: #94a3b8; font-size: 1.2rem;">=</div>
                        <div style="text-align: center; background: rgba(16, 185, 129, 0.1); padding: 5px 15px; border-radius: 10px;">
                            <div style="font-size: 0.7rem; color: #10b981; text-transform: uppercase; font-weight: bold;">Natija</div>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; color: #059669; letter-spacing: 2px; font-weight: bold;">{b_res}</div>
                        </div>
                    </div>
                    """
                
                st.markdown(rows_v, unsafe_allow_html=True)
                if len(ver_text) > 5:
                    st.caption(f"Dastlabki 5 ta belgi ko'rsatildi (Jami: {len(ver_text)})")
                
                # --- Simplified Vernam Explanation ---
                st.markdown("""
                    <div class="glass-card fade-in" style="margin-top: 2rem; border-left: 4px solid #4b4bff; background: rgba(75, 75, 255, 0.02);">
                        <h3 style="color: #4b4bff;">🔢 Vernam (XOR) qanday ishlaydi?</h3>
                        <p style="font-size: 1.1rem; line-height: 1.6;">
                            Bu shifr kompyuterning eng tub darajasida — <b>bitlar</b> bilan ishlaydi:
                        </p>
                        <ul style="padding-left: 20px;">
                            <li style="margin-bottom: 10px;"><b>0 ⊕ 0 = 0</b> va <b>1 ⊕ 1 = 0</b> (Bir xil bo'lsa - 0)</li>
                            <li style="margin-bottom: 10px;"><b>0 ⊕ 1 = 1</b> va <b>1 ⊕ 0 = 1</b> (Har xil bo'lsa - 1)</li>
                        </ul>
                        <div style="background: white; padding: 15px; border-radius: 10px; border: 1px dashed #4b4bff; margin-top: 10px;">
                            💡 <b>Qiziqarli fakt:</b> Agar shifrlangan natijani yana o'sha kalitga XOR qilsangiz, asl matn qaytib chiqadi. Shuning uchun shifrlash va deshifrlash tugmasi bu yerda bitta!
                        </div>
                    </div>
                """, unsafe_allow_html=True)

def render_rsa():
    st.markdown("""
        <div class="glass-card fade-in" style="margin-bottom: 2rem;">
            <h2 style="margin: 0; display: flex; align-items: center; gap: 15px;">
                <i class="fa-solid fa-lock" style="color: #6366f1;"></i> 
                RSA Professional Algoritmi
            </h2>
            <p style="color: #666; margin-top: 10px;">Zamonaviy dunyoning eng xavfsiz shifrlash tizimi — ochiq kalitli kriptografiya.</p>
        </div>
    """, unsafe_allow_html=True)
    
    rsa_tabs = st.tabs(["🔑 Kalitlar Markazi", "🔒 Shifrlash", "🔓 Deshifrlash", "📖 Matematik Lab"])
    
    with rsa_tabs[0]:
        col1, col2 = st.columns([1, 1.2])
        with col1:
            st.markdown("""
                <div style="background: rgba(99, 102, 241, 0.05); padding: 1.5rem; border-radius: 20px; border: 1px dashed #6366f1;">
                    <h4 style="margin-top:0;">🔐 Kalitlarni Yaratish</h4>
                    <p style="font-size: 0.9rem; color: #555;">RSA xavfsizligi ikki katta tub sonning ko'paytmasiga asoslanadi.</p>
                </div>
            """, unsafe_allow_html=True)
            st.write("")
            bits = st.select_slider("Xavfsizlik darajasi (bits)", options=[512, 1024, 2048], value=1024)
            if st.button("🚀 Yangi Kalitlar Generatorini Ishga Tushirish", use_container_width=True):
                with st.spinner("Murakkab matematik hisob-kitoblar bajarilmoqda..."):
                    manager = rsa.RSAManager(bits=bits)
                    manager.generate_keys()
                    st.session_state.rsa_manager = manager
                    st.session_state.rsa_public = (manager.e, manager.n)
                    st.session_state.rsa_private = (manager.d, manager.n)
                    st.success(f"✅ {bits}-bitli xavfsiz kalitlar yaratildi!")
        
        with col2:
            if 'rsa_public' in st.session_state:
                # Digital Key Cards
                st.markdown(f"""
                    <div style="display: grid; gap: 1rem;">
                        <div class="glass-card fade-in" style="border-left: 5px solid #6366f1; padding: 1.2rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                                <b style="color: #6366f1;"><i class="fa-solid fa-globe"></i> OCHIQ KALIT (PUBLIC)</b>
                                <span style="font-size: 0.7rem; background: #6366f1; color: white; padding: 2px 8px; border-radius: 10px;">XAVFSIZ</span>
                            </div>
                            <div style="font-family: monospace; font-size: 0.8rem; background: #f8fafc; padding: 10px; border-radius: 8px; word-break: break-all; color: #334155;">
                                {st.session_state.rsa_public}
                            </div>
                            <small style="color: #94a3b8; margin-top: 5px; display: block;">* Bu kalitni hamma bilan baham ko'rish mumkin.</small>
                        </div>
                        <div class="glass-card fade-in" style="border-left: 5px solid #ef4444; padding: 1.2rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                                <b style="color: #ef4444;"><i class="fa-solid fa-key"></i> YOPIQ KALIT (PRIVATE)</b>
                                <span style="font-size: 0.7rem; background: #ef4444; color: white; padding: 2px 8px; border-radius: 10px;">MAXFIY</span>
                            </div>
                            <div style="font-family: monospace; font-size: 0.8rem; background: #fef2f2; padding: 10px; border-radius: 8px; word-break: break-all; color: #991b1b;">
                                {st.session_state.rsa_private}
                            </div>
                            <small style="color: #94a3b8; margin-top: 5px; display: block;">* Bu kalitni HECH KIMGA bermang!</small>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style="height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #f8fafc; border-radius: 20px; border: 2px dashed #e2e8f0; color: #94a3b8;">
                        <i class="fa-solid fa-shield-slash" style="font-size: 3rem; margin-bottom: 1rem;"></i>
                        <div>Kalitlar hali yaratilmagan</div>
                    </div>
                """, unsafe_allow_html=True)

    with rsa_tabs[1]:
        st.subheader("🔒 Ma'lumotni Shifrlash (OAEP)")
        encrypt_text = st.text_area("Shifrlash uchun matn", placeholder="Maxfiy xabarni kiriting...", key="enc_text")
        
        if st.button("Shifrlash", key="btn_encrypt", use_container_width=True):
            if encrypt_text and 'rsa_manager' in st.session_state:
                try:
                    manager = st.session_state.rsa_manager
                    cipher = manager.encrypt(encrypt_text)
                    st.session_state.last_rsa_cipher = str(cipher)
                    st.session_state.last_rsa_mode = "OAEP"
                    st.success("✅ Shifrlash OAEP padding bilan bajarildi!")
                except ValueError as ve:
                    if "Kalit juda kichik" in str(ve):
                        # Fallback to Textbook RSA
                        manager = st.session_state.rsa_manager
                        cipher = manager.textbook_encrypt(encrypt_text)
                        st.session_state.last_rsa_cipher = str(cipher)
                        st.session_state.last_rsa_mode = "Textbook"
                        st.warning(f"""
                            ⚠️ **Zaif Shifrlash Rejimi Faollashtirildi**
                            
                            Kalit juda kichik bo'lgani uchun xavfsiz OAEP padding ishlatib bo'lmadi. 
                            Tizim **'Textbook RSA'** (soda) usuliga o'tdi. Bu usul professional darajada xavfsiz emas!
                        """)
                    else:
                        st.error(f"Xatolik: {str(ve)}")
                except Exception as e:
                    st.error(f"Xatolik: {str(e)}")
            elif not encrypt_text:
                st.error("Matnni kiriting!")
            else:
                st.error("Avval kalitlarni yarating!")
        
        if 'last_rsa_cipher' in st.session_state:
            render_result("Shifrlangan Matn (Ciphertext)", st.session_state.last_rsa_cipher)
            if st.button("🔄 Natijani deshifrlash oynasiga yuborish", key="copy_rsa"):
                st.session_state.dec_input = st.session_state.last_rsa_cipher
                st.rerun()

    with rsa_tabs[2]:
        st.subheader("🔓 Ma'lumotni Deshifrlash (CRT)")
        decrypt_input = st.text_area("Shifrlangan sonni kiriting", value=st.session_state.get('last_rsa_cipher', ""), key="dec_input")
        
        if st.button("Deshifrlash", key="btn_decrypt", use_container_width=True):
            if decrypt_input and 'rsa_manager' in st.session_state:
                try:
                    manager = st.session_state.rsa_manager
                    # Check which mode we are in based on input format
                    if decrypt_input.startswith("["):
                        # Textbook mode (list of ints)
                        import ast
                        cipher_list = ast.literal_eval(decrypt_input)
                        decrypted = manager.textbook_decrypt(cipher_list)
                        st.success("✅ Deshifrlash (Textbook) yakunlandi!")
                    else:
                        # Professional mode (single large int)
                        ciphertext = int(decrypt_input)
                        decrypted = manager.decrypt(ciphertext)
                        st.success("✅ Deshifrlash (CRT + OAEP) yakunlandi!")
                    
                    st.session_state.last_rsa_decrypted = decrypted
                except Exception as e:
                    st.error(f"Xatolik: {str(e)}")
            elif not decrypt_input:
                st.error("Shifrlangan ma'lumotni kiriting!")
            else:
                st.error("Kalitlar mavjud emas!")
        
        if 'last_rsa_decrypted' in st.session_state:
            render_result("Asl Ma'lumot", st.session_state.last_rsa_decrypted)

    with rsa_tabs[3]:
        st.subheader("📖 RSA Matematik Jarayoni Vizualizatsiyasi")
        st.write("Bu yerda professional RSA dagi 'parda ortidagi' amallarni kuzatishingiz mumkin.")
        
        if 'rsa_manager' not in st.session_state:
            st.warning("Avval 'Kalitlar Yaratish' bo'limida kalit yarating.")
        else:
            manager = st.session_state.rsa_manager
            
            # Stage 1: Prime Generation
            with st.expander("1-Bosqich: Katta Tub Sonlar Qayerdan Keladi?"):
                st.markdown("""
                    Professional RSA da $p$ va $q$ shunchaki tanlanmaydi, balki tasodifiy generatsiya qilinib, **Miller-Rabin** testi orqali tekshiriladi.
                """)
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**P:** {str(manager.p)[:30]}...")
                    st.write(f"Bit uzunligi: {manager.p.bit_length()} bit")
                with col2:
                    st.info(f"**Q:** {str(manager.q)[:30]}...")
                    st.write(f"Bit uzunligi: {manager.q.bit_length()} bit")
                
                st.markdown("""
                    **Miller-Rabin Algoritmi:** Bu ehtimollikka asoslangan test bo'lib, sonning tubligini bir necha raund davomida tekshiradi. 
                    Agar son testdan o'tsa, u **'Prime Candidate'** (Tublikka nomzod) deb ataladi.
                """)

            # Stage 2: Modulus & Phi
            with st.expander("2-Bosqich: Modul ($n$) va Eyler Funksiyasi ($\phi$)"):
                st.latex(rf"n = p \times q = {manager.n}")
                phi = (manager.p - 1) * (manager.q - 1)
                st.latex(rf"\phi(n) = (p-1)(q-1) = {phi}")
                
                st.markdown("---")
                st.markdown("**CRT (Chinese Remainder Theorem) parametrlari:**")
                st.latex(rf"dp = d \pmod{{(p-1)}} = {manager.dp}")
                st.latex(rf"dq = d \pmod{{(q-1)}} = {manager.dq}")
                st.markdown("""
                    Bu parametrlar deshifrlashni tezlashtirish uchun kerak. 
                    Katta $d$ darajasiga ko'tarish o'rniga, kichikroq $dp$ va $dq$ darajalaridan foydalaniladi.
                """)

            # Stage 3: EEA Calculation for d
            with st.expander("3-Bosqich: Kengaytirilgan Evklid Algoritmi (EEA)"):
                st.markdown(f"Bizga shunday $d$ kerakki: $e \cdot d \equiv 1 \pmod{{\phi(n)}}$. Hozirgi $e = {manager.e}$.")
                
                # Use current keys for EEA table
                demo_a, demo_b = manager.e, phi
                
                from logic.prime_utils import extended_gcd_steps
                _, x, _, steps = extended_gcd_steps(demo_a, demo_b)
                
                import pandas as pd
                df_steps = pd.DataFrame(steps)
                # Convert all columns to string to avoid "int too big to convert" OverflowError
                df_steps = df_steps.astype(str)
                
                if len(df_steps) > 15:
                    st.info(f"💡 Algoritm juda ko'p ({len(df_steps)}) qadamdan iborat. Dastlabki va oxirgi qadamlarni ko'rsatamiz:")
                    st.table(pd.concat([df_steps.head(5), df_steps.tail(5)]))
                else:
                    st.table(df_steps)
                
                st.success(f"Natijada hisoblangan modular inverse $d$: {manager.d}")
                st.markdown(f"**Isbot:** $({manager.e} \\times {manager.d}) \\pmod{{{phi}}} = 1$")

            # Stage 4: Encryption Logic (OAEP vs Textbook)
            with st.expander("4-Bosqich: Shifrlash Strategiyasi"):
                k = manager.bits // 8
                hLen = 32
                if k < 2 * hLen + 2:
                    st.warning("⚠️ Kichik tub sonlar ishlatilmoqda. OAEP padding uchun joy yetarli emas.")
                    st.markdown("""
                        Siz tanlagan sonlar juda kichik bo'lgani uchun tizim **'Textbook RSA'** (oddiy darajaga ko'tarish) usulidan foydalanadi.
                        Matematik formula: $C = M^e \pmod n$
                    """)
                    sample_m = 42
                    st.latex(rf"C = {sample_m}^{{{manager.e}}} \pmod{{{manager.n}}} = {pow(sample_m, manager.e, manager.n)}")
                else:
                    st.success("✅ Professional RSA (OAEP) rejimi faol.")
                    st.markdown("""
                        Katta sonlar bilan biz **OAEP** ishlatamiz. Bu xabarni quyidagicha o'zgartiradi:
                        1. Xabarga tasodifiy 'Seed' qo'shiladi.
                        2. XOR operatsiyalari orqali xabar taniy bo'lmas darajaga keltiriladi.
                        3. Faqat shundan keyin darajaga ko'tariladi.
                    """)

def render_hash():
    st.markdown('<div class="glass-card fade-in"><h2><i class="fa-solid fa-fingerprint"></i> Xesh Funksiyalar (SHA-256)</h2></div>', unsafe_allow_html=True)
    
    st.subheader("Avalanche Effect (Ko'chki Effekti)")
    t1 = st.text_input("1-Matn", value="Salom Dunyo")
    t2 = st.text_input("2-Matn (O'zgartirilgan)", value="Salom Dunya")
    
    if t1 and t2:
        result = hashing.avalanche_effect(t1, t2)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**1-Xesh:**")
            st.code(result['hash1'])
        with c2:
            st.markdown("**2-Xesh:**")
            st.code(result['hash2'])
            
        st.markdown(f"""
            <div class="glass-card" style="text-align: center;">
                <h3 style="color: #ffffff;">O'zgarish Darajasi</h3>
                <div style="font-size: 3rem; font-weight: 700;">{result['percentage']}%</div>
                <p>{result['diff_bits']} bit 256 tadan farq qiladi.</p>
            </div>
        """, unsafe_allow_html=True)

def render_library():
    st.markdown('<div class="glass-card fade-in"><h2><i class="fa-solid fa-book-bookmark"></i> Kriptografiya Kutubxonasi</h2></div>', unsafe_allow_html=True)
    
    techs = [
        {
            "id": "caesar",
            "title": "Sezar Shifri",
            "short": "Alifbo harflarini ma'lum bir pozitsiyaga siljitish usuli.",
            "sections": [
                {"title": "1. Sarlavha va Kirish", "content": "Sezar usuli. Sezar shifri oddiy siljitish shifrining bir qismi hisoblanadi. Bu shifrni rimlik imperator Gole Yuliy Sezar o‘ylab topgan. Uning asosiy vazifasi oddiy matnni alifbodagi harflarni siljitish orqali taniy bo'lmas holatga keltirishdir."},
                {"title": "2. Matematik Model", "content": "Shifrlashda matnning har bir harfi boshqa harf bilan quyidagi qoida asosida almashtiriladi. Harflarni almashtirishda kelayotgan yozuv harflarini k-ga siljitib almashtiriladi. Bu yerda M – butun son hisoblanib, ochiq matni belgisini biror alfavitdagi o‘rni, S – butun son bo‘lib, shifr belgini biror alfavitdagi o‘rni. C=(M+k)modm, m - alfavit uzunligi. Deshifrlash ifodasi esa M=(C-k)modm ifoda bilan ifodalanadi. Yuliy Sezar bevosita k = 3 bo‘lganda ushbu usuldan foylangan."},
                {"title": "3. Texnik Xususiyatlar va Kamchiliklari", "content": "Sezar usulining kamchiligi bu bir xil harflarning o‘z navbatida, bir xil harflarga almashishidir. Bu esa chastotali tahlil (frequency analysis) yordamida shifrni oson buzilishiga olib keladi."},
                {"title": "4. Misol", "content": "Masalan, matn sifatida T0=KOMPUTER so‘zini va K=3 deb oladigan bo‘lsak Sezar usuli natijasida quyidagi shifrlangan yozuv hosil bo‘ladi: T1 = NRPSXWHU."},
                {"title": "5. Vizualizatsiya", "content": "Diagramma tavsifi: Ikkita konsentrik alifbo halqasi tasvirlanadi. Ichki halqa tashqi halqaga nisbatan K qadamga aylantirilgan."}
            ],
            "img": "caesar_cipher_diagram_1776755063450.png"
        },
        {
            "id": "vigenere",
            "title": "Vigenere Shifri",
            "short": "Polialfavitli shifrlash tizimi (Murakkab Sezar).",
            "sections": [
                {"title": "1. Sarlavha va Kirish", "content": "Vijiner shifri. Birinchi bo‘lib, Vijiner tizimi 1586-yilda chop etilgan va u ko‘p alifboli tizimga nisbatan Yuqoriroq o‘rinda turadi. Bleza Vijinera o‘zini XVI asrning fransuz diplomati deb hisoblaydi."},
                {"title": "2. Matematik Model", "content": "Bunday ko‘p alifboli almashtirish shifrini shifrlash jadvali orqali ifodalash mumkin. Har bir matn harfi kalitning mos harfiga qarab siljitiladi. C[i] = (P[i] + K[i mod L]) mod 26."},
                {"title": "3. Texnik Xususiyatlar va Effektlar", "content": "Polialfavitli tabiat harflarning statistik chastotasini yashiradi. Quyidagi jadvallarda Vijinerning ingliz alifbosi va kiril alifbolari uchun mos keluvchi qiymatlar ko‘rsatilgan."},
                {"title": "4. Amaliy Qo'llanilishi", "content": "Vigenere shifri klassik kriptografiya tarixida burilish nuqtasi bo'lgan. U tushunish oson bo'lgan murakkab simmetrik tizim sifatida o'qitiladi."},
                {"title": "5. Vizualizatsiya", "content": "Diagramma tavsifi: 'Tabula Recta' - 26x26 o'lchamli alifbo jadvali. Satrlar - matn harflari, ustunlar - kalit harflari."}
            ],
            "img": None
        },
        {
            "id": "rsa",
            "title": "RSA Algoritmi",
            "short": "Ochiq kalitli asimmetrik shifrlash texnologiyasi.",
            "sections": [
                {"title": "1. Sarlavha va Kirish", "content": "RSA (Rivest-Shamir-Adleman) - dunyodagi birinchi va eng mashhur asimmetrik kriptotizim. 1977 yilda kashf etilgan ushbu algoritm zamonaviy kiberxavfsizlikning asosi hisoblanadi. U ochiq aloqa kanallari orqali xavfsiz ma'lumot almashish imkonini beradi."},
                {"title": "2. Matematik Model", "content": "RSA ikki katta tub sonning ko'paytmasini faktorlarga ajratish qiyinligiga asoslangan.\n1. n = p * q, phi = (p-1)*(q-1)\n2. e tanlanadi: gcd(e, phi) = 1\n3. d topiladi: e*d = 1 mod phi\nShifrlash: C = M^e mod n\nDeshifrlash: M = C^d mod n"},
                {"title": "3. Texnik Xususiyatlar va Effektlar", "content": "RSA asimmetrik tizim bo'lib, ikkita kalit (ochiq va maxfiy) ishlatadi. OAEP padding usuli 'Textbook RSA' zaifliklarini bartaraf etish uchun zarur. Kalit uzunligi kamida 2048 bit bo'lishi tavsiya etiladi."},
                {"title": "4. Amaliy Qo'llanilishi", "content": "RSA bugun SSL/TLS (HTTPS), raqamli imzolar va SSH protokollarida keng qo'llaniladi. U onlayn bank tizimlari va elektron tijorat xavfsizligini ta'minlovchi asosiy texnologiyadir."},
                {"title": "5. Vizualizatsiya", "content": "Diagramma tavsifi: Alisa va Bob o'rtasidagi aloqa. Alisa Bobning ochiq kaliti bilan shifrlaydi, Bob esa o'zining yopiq kaliti bilan ochadi. Kalitlar juftligi va modul amali markaziy o'rinni egallaydi."}
            ],
            "img": None
        },
        {
            "id": "vernam",
            "title": "Vernam Shifri",
            "short": "Ikkilik sanoq sistemasida XOR amali asosida shifrlash.",
            "sections": [
                {"title": "1. Sarlavha va Kirish", "content": "Vernam shifri. Vernamning shifrlash tizimi modul qiymati m=2 bo‘lgan Vijiner shifrlash tizimining bir qismi hisoblanib, 1926-yilda bu usulning aniq ko‘rinishi ishlab chiqiladi."},
                {"title": "2. Matematik Model", "content": "Gilbertom Vernam AT&SSHA firmasi xomiyligi ostida kiruvchi matn sifatida ikkilik sanoq sistemasidan foydalandi. Shifrlash formulasi: y = x XOR k. Deshifrlash uchun shifrmatn va kalit yana XOR qilinadi."},
                {"title": "3. Texnik Xususiyatlar", "content": "Matnning har bir harfi 5-bit bo‘lakli (b0,b1…b4) Bado raqami bilan kodlanadi. Ixtiyoriy ketma-ketlikdagi ikkilik kalitlar k0,k1,k2, avval kitobsimon lentaga yoziladi."},
                {"title": "4. Xavfsizlik", "content": "Agar kalit tasodifiy bo'lsa va uzunligi matn bilan teng bo'lsa, bu shifr 'Perfect Secrecy' (mutlaq xavfsizlik) ga ega bo'ladi."},
                {"title": "5. Vizualizatsiya", "content": "Diagramma tavsifi: Kiruvchi x va kalit k mantiqiy XOR blokiga kiradi va natija y hosil bo'ladi."}
            ],
            "img": None
        },
        {
            "id": "sha256",
            "title": "SHA-256 Xesh",
            "short": "Ma'lumotlar yaxlitligini tekshirish uchun xavfsiz xesh.",
            "sections": [
                {"title": "1. Sarlavha va Kirish", "content": "SHA-256 (Secure Hash Algorithm 256) - ma'lumotlarning qaytmas 'barmoq izi'ni yaratuvchi funksiya. NIST tomonidan standartlashtirilgan. U har qanday uzunlikdagi ma'lumotni 256-bitli (32 bayt) qat'iy uzunlikdagi natijaga aylantiradi."},
                {"title": "2. Matematik Model", "content": "Algoritm 512-bitli bloklarda ishlaydi va 64 raunddan iborat siqish funksiyasini qo'llaydi. Asosiy mantiqiy amallar:\n- XOR, AND, NOT\n- ROTR (Rotate Right) va SHR (Shift Right)\n- Modulo 2^32 qo'shish amali. Bu amallar ma'lumotni qaytarib bo'lmas darajada aralashtirib tashlaydi."},
                {"title": "3. Texnik Xususiyatlar va Effektlar", "content": "Eng muhim xususiyati - 'Ko'chki effekti' (Avalanche Effect). Agar kiruvchi ma'lumotning birgina biti o'zgarsa, natija (xesh) butunlay o'zgaradi. Shuningdek, u to'qnashuvga (collision) chidamlidir."},
                {"title": "4. Amaliy Qo'llanilishi", "content": "SHA-256 blokcheyn texnologiyasi (Bitcoin mining), parollarni xavfsiz saqlash va dasturiy ta'minotning yaxlitligini (checksum) tekshirishda standart hisoblanadi."},
                {"title": "5. Vizualizatsiya", "content": "Diagramma tavsifi: Kiruvchi xabar bloklarga bo'linadi, har bir blok siqish funksiyasi orqali o'tadi va oldingi blokning natijasi bilan 'XOR' amali orqali bog'lanadi (Merkle-Damgard tuzilmasi)."}
            ],
            "img": None
        }
    ]
    
    cols = st.columns(2)
    for i, tech in enumerate(techs):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"### {tech['title']}")
                st.write(tech['short'])
                
                # Academic PDF Download
                pdf_bytes = pdf_gen.generate_academic_pdf(tech['title'], tech['sections'], tech['img'])
                st.download_button(
                    label="🎓 Akademik PDF Yuklab Olish",
                    data=pdf_bytes,
                    file_name=f"{tech['id']}_academic_guide.pdf",
                    mime="application/pdf"
                )

# Helper for styled result containers
def render_result(title, content):
    st.markdown(f"""
        <div class="glass-card fade-in" style="border-left: 5px solid #4bff4b; background: rgba(75, 255, 75, 0.05); padding: 1.5rem; margin-top: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.5rem;">
                <i class="fa-solid fa-circle-check" style="color: #2eb82e; font-size: 1.2rem;"></i>
                <small style="color: #2eb82e; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">{title}</small>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.8rem; color: #333; word-break: break-all; letter-spacing: 2px;">
                {content}
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main App Logic
render_header()
st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
if st.session_state.page == 'Home':
    render_home()
elif st.session_state.page == 'Classical':
    render_classical()
elif st.session_state.page == 'RSA':
    render_rsa()
elif st.session_state.page == 'Hash':
    render_hash()
elif st.session_state.page == 'Library':
    render_library()
