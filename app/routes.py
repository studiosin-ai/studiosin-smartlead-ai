from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIServiceError, ai_service


pages = Blueprint("pages", __name__)
api = Blueprint("api", __name__)


@pages.route("/")
def index():
    return render_template("index.html")


@pages.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api.route("/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json() or {}

    mesaj = data.get("mesaj", "").strip()
    gecmis = data.get("gecmis", [])

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj boş bırakılamaz."
        }), 400

    try:
        yanit = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify({
            "basari": True,
            "yanit": yanit
        })

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zeka servisine şu anda ulaşılamıyor."
        }), 503


@api.route("/leads", methods=["POST"])
def lead_kaydet():
    data = request.get_json() or {}

    isim = data.get("isim", "").strip()
    telefon = data.get("telefon", "").strip()
    mesaj = data.get("mesaj", "").strip()

    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon zorunludur."
        }), 400

    lead_ekle(isim, telefon, mesaj)

    return jsonify({
        "basari": True,
        "mesaj": "Bilgileriniz başarıyla kaydedildi."
    }), 201


@api.route("/leads", methods=["GET"])
def leadleri_getir():
    leadler = tum_leadler()

    return jsonify({
        "basari": True,
        "leadler": [dict(lead) for lead in leadler]
    })
