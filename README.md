---
license: apache-2.0
language:
- en
tags:
- computer-vision
- football
- object-detection
- multi-object-tracking
author: Assem Sabry
pretty_name: Whistle
---

# Whistle

![Whistle official poster](media/whistle-poster.png)

**Whistle** is developed and owned by [Assem Sabry](https://assem.one/).

Whistle يحوّل فيديو مباراة كرة القدم إلى بيانات زمنية قابلة للفحص: detections وtracks وملفات JSON/CSV وفيديو مرئي. لا يحدد أسماء اللاعبين أو مراكزهم أو أرقام قمصانهم، ولا يحتوي على مهمة تقييم للاعبين.

## الحالة الحالية

الإصدار `0.0.1` يوفّر:

- قراءة manifest للفيديو والتحقق من الملف.
- schema ثابت للـ frames وdetections وtracks.
- CLI يستقبل MP4 ويكتب manifest ونتيجة JSON أولية قابلة لإعادة التشغيل.
- طبقة detector/tracker قابلة للاستبدال دون ربطها بمكتبة بعينها.

لا توجد أوزان أو بيانات فيديو موزعة مع المستودع. يجب تسجيل provenance والترخيص قبل إضافة أي dataset أو checkpoint.

## التشغيل

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
whistle inspect path\to\match.mp4 --output outputs\match
pytest
```

## مراحل المنتج

Core ثم Pitch ثم Ball ثم Events الأساسية ثم Analytics. لن تظهر السرعة أو المسافة عند فشل معايرة الكاميرا أو انخفاض الثقة.

## الترخيص

الكود الأصلي Apache-2.0. رخصة الأوزان والبيانات منفصلة وتُراجع قبل النشر؛ لا تُضمّن فيديوهات المباريات أو مشتقاتها دون حق إعادة التوزيع.
