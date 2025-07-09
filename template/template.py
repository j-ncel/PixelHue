from string import Template


css = """
<style>
.stColumns > div {
    align-items: flex-start;
    justify-content: center;
    display: flex;
    flex-direction: column;
}

.color-text {
    font-size: 1em;
    font-family: monospace;
    text-align: center;
    width: 100px;
}
</style>
"""

color_swatch_template = Template("""
<div style="
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
">
    <div
        class="color-block"
        style="background:${color};"
        onclick="copyColor('${color}', this)"
        title="Click to copy ${color}"
    >
        <span class="copy-feedback">Copied!</span>
    </div>
</div>

<style>
.color-block {
    width: 100px;
    height: 100px;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out;
}

.color-block:hover {
    transform: scale(1.05);
}

.copy-feedback {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.5);
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 8px 12px;
    border-radius: 5px;
    font-size: 0.9em;
    font-family: monospace;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease-out, transform 0.4s ease-out;
    white-space: nowrap;
    z-index: 10;
}
</style>

<script>
function copyColor(colorValue, element) {
    navigator.clipboard
        .writeText(colorValue)
        .then(function () {
            const feedbackSpan = element.querySelector(".copy-feedback");
            if (feedbackSpan) {
                feedbackSpan.style.transition = "none";
                feedbackSpan.style.opacity = "0";
                feedbackSpan.style.transform = "translate(-50%, -50%) scale(0.5)";

                void feedbackSpan.offsetWidth; 

                feedbackSpan.style.transition = "opacity 0.4s ease-out, transform 0.4s ease-out";
                feedbackSpan.style.opacity = "1";
                feedbackSpan.style.transform = "translate(-50%, -50%) scale(1)";

                setTimeout(() => {
                    feedbackSpan.style.opacity = "0";
                    feedbackSpan.style.transform = "translate(-50%, -50%) scale(0.8)";
                }, 800);
            }
        });
}
</script>
""")
