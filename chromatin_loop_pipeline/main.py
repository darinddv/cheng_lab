from pipeline.config_loader import load_config
from pipeline.download_encode import download_all_epigenetics
from pipeline.liftover_utils import liftover_all
from pipeline.loop_processing import load_loops, extract_anchors, annotate_anchors
from pipeline.bins import build_bins, annotate_bins
from pipeline.reporting import save_outputs

def main():
    cfg = load_config("config/example_gm12878.yaml")

    download_all_epigenetics(cfg)
    liftover_all(cfg)

    loops = load_loops(cfg)
    anchors1, anchors2 = extract_anchors(loops)

    bins = build_bins(cfg)
    bins = annotate_bins(bins, cfg)

    anchors = annotate_anchors(anchors1, anchors2, cfg)

    save_outputs(bins, anchors, loops, cfg)

if __name__ == "__main__":
    main()
