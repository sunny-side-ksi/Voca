"""
docling-mcp 가 사용하는 HuggingFace 모델을 심볼릭 링크 없이 다운로드.
Windows에서 심볼릭 링크 권한 없이 동작하도록 local_dir_use_symlinks=False 사용.
"""
from pathlib import Path
from huggingface_hub import snapshot_download

MODEL_DIR = Path.home() / ".cache" / "docling_models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

MODELS = [
    "ds4sd/docling-models",
    "ds4sd/DocLayNet",
]

for repo_id in MODELS:
    local_dir = MODEL_DIR / repo_id.replace("/", "--")
    print(f"다운로드 중: {repo_id} → {local_dir}")
    try:
        path = snapshot_download(
            repo_id=repo_id,
            local_dir=str(local_dir),
            local_dir_use_symlinks=False,
            ignore_patterns=["*.msgpack", "flax_model*", "tf_model*", "rust_model*"],
        )
        print(f"  완료: {path}")
    except Exception as e:
        print(f"  오류: {e}")

print("\n모든 모델 다운로드 완료.")
print(f"모델 경로: {MODEL_DIR}")
