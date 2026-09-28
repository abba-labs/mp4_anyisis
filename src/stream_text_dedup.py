"""
stream_text_dedup.py - 滑动窗口连续流式文本去重引擎
在 OCR 逐帧提取的基础上，建立时间空间平移队列，逐行消除重合带，提取全量原生文本
"""

def deduplicate_text_stream(frames_ocr_lines, window_size=35):
    accumulated_doc = []
    
    for f in frames_ocr_lines:
        lines = f.get('lines', [])
        for l in lines:
            clean = l.strip()
            if any(k in clean for k in ['ETMCU', '保密', '未经授权', '第', 'V1.0', 'V 1.0']):
                continue
            if len(clean) < 2:
                continue
            
            recent = [item['text'] for item in accumulated_doc[-window_size:]]
            is_dup = False
            for r in recent:
                if clean == r or (len(clean) > 8 and clean in r) or (len(r) > 8 and r in clean):
                    is_dup = True
                    break
            
            if not is_dup:
                accumulated_doc.append({'frame': f.get('frame', ''), 'text': clean})
                
    return accumulated_doc
