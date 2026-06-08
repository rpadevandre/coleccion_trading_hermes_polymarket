import { useMemo, useState, type CSSProperties, type ComponentType } from 'react';
import Landing from './views/Landing';
import ROICalculator from './views/ROICalculator';
import DemoCallFlow from './views/DemoCallFlow';
import FreeAuditForm from './views/FreeAuditForm';
import PilotSignup from './views/PilotSignup';
import { businessMeta, frontendViews, type RouteKey } from './businessMeta';
import './styles.css';

export type ViewProps = {
  onNavigate: (route: RouteKey) => void;
};

const routes: Record<RouteKey, ComponentType<ViewProps>> = {
  landing: Landing,
  roi: ROICalculator,
  demo: DemoCallFlow,
  audit: FreeAuditForm,
  pilot: PilotSignup
};

export default function App() {
  const [route, setRoute] = useState<RouteKey>('landing');
  const ActiveView = useMemo(() => routes[route], [route]);
  const activeMeta = frontendViews.find((view) => view.key === route) ?? frontendViews[0];

  return (
    <div className="app-shell" style={{ '--accent': businessMeta.accent, '--accent-dark': businessMeta.accentDark } as CSSProperties}>
      <nav className="top-nav" aria-label="HVAC missed-call recovery prototype sections">
        <button className="brand-button" type="button" onClick={() => setRoute('landing')} aria-label="Return to landing page">
          <span className="brand-mark">A</span>
          <span>
            <strong>{businessMeta.shortName}</strong>
            <small>Concierge validation prototype</small>
          </span>
        </button>
        <div className="nav-actions" role="tablist" aria-label="Prototype views">
          {frontendViews.map((view) => (
            <button
              key={view.key}
              type="button"
              role="tab"
              aria-selected={route === view.key}
              onClick={() => setRoute(view.key)}
              className={route === view.key ? 'active' : ''}
            >
              {view.navLabel}
            </button>
          ))}
        </div>
      </nav>

      <div className="route-context" aria-live="polite">
        <span>Current view</span>
        <strong>{activeMeta.name}</strong>
        <p>{activeMeta.primaryOutcome}</p>
      </div>

      <ActiveView onNavigate={setRoute} />
    </div>
  );
}
